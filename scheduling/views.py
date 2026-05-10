"""Scheduling App - Swekchya
Schedule meetings, upcoming/weekly/monthly views
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.models import User
from teams.models import Team
from core.models import AuditLog
from .models import Meeting
import datetime


@login_required
def schedule_list(request):
    now = timezone.now()
    view = request.GET.get('view', 'upcoming')
    if view == 'weekly':
        end = now + datetime.timedelta(days=7)
        meetings = Meeting.objects.filter(date_time__range=(now, end))
    elif view == 'monthly':
        end = now + datetime.timedelta(days=30)
        meetings = Meeting.objects.filter(date_time__range=(now, end))
    else:
        meetings = Meeting.objects.filter(date_time__gte=now)
    my_meetings = (meetings.filter(attendees=request.user) | meetings.filter(organiser=request.user)).distinct()
    return render(request, 'scheduling/schedule_list.html', {
        'meetings': my_meetings.select_related('team', 'organiser'),
        'view': view, 'now': now,
    })


@login_required
def schedule_meeting(request):
    teams = Team.objects.filter(status='active')
    users = User.objects.exclude(pk=request.user.pk)
    preselected_team = request.GET.get('team')

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        date_str = request.POST.get('date_time', '')
        platform = request.POST.get('platform', 'zoom')
        meeting_link = request.POST.get('meeting_link', '')
        agenda = request.POST.get('agenda', '')
        team_id = request.POST.get('team')
        attendee_ids = request.POST.getlist('attendees')

        if not title or not date_str:
            messages.error(request, 'Title and date/time are required.')
        else:
            try:
                date_time = datetime.datetime.fromisoformat(date_str)
                if timezone.is_naive(date_time):
                    date_time = timezone.make_aware(date_time)
                meeting = Meeting(
                    title=title, organiser=request.user, date_time=date_time,
                    platform=platform, meeting_link=meeting_link, agenda=agenda,
                )
                if team_id:
                    try:
                        meeting.team = Team.objects.get(pk=team_id)
                    except Team.DoesNotExist:
                        pass
                meeting.save()
                if attendee_ids:
                    meeting.attendees.set(User.objects.filter(pk__in=attendee_ids))
                meeting.attendees.add(request.user)
                AuditLog.objects.create(
                    user=request.user, action_type='insert',
                    table_name='Meeting', record_id=meeting.id,
                    description=f"Meeting '{title}' scheduled for {date_time.strftime('%d %b %Y %H:%M')}"
                )
                messages.success(request, f'Meeting "{title}" scheduled successfully.')
                return redirect('schedule_list')
            except ValueError as e:
                messages.error(request, f'Invalid date: {e}')

    return render(request, 'scheduling/schedule_meeting.html', {
        'teams': teams, 'users': users,
        'platforms': Meeting.PLATFORM_CHOICES,
        'preselected_team': preselected_team,
    })


@login_required
def meeting_detail(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk)
    return render(request, 'scheduling/meeting_detail.html', {'meeting': meeting})


@login_required
def delete_meeting(request, pk):
    meeting = get_object_or_404(Meeting, pk=pk, organiser=request.user)
    AuditLog.objects.create(
        user=request.user, action_type='delete',
        table_name='Meeting', record_id=meeting.id,
        description=f"Meeting '{meeting.title}' deleted"
    )
    meeting.delete()
    messages.success(request, 'Meeting deleted.')
    return redirect('schedule_list')
