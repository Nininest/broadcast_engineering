"""Teams App - Yujala
Display teams, search, email team, schedule meeting, skills, dependencies
"""
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from teams.models import Team, TeamMember, TeamDependency, CodeRepository, ContactChannel
from organization.models import Department
from core.models import AuditLog
from .forms import TeamEmailForm


@login_required
def team_list(request):
    query = request.GET.get('q', '')
    dept_filter = request.GET.get('dept', '')
    status_filter = request.GET.get('status', '')
    teams = Team.objects.select_related('department', 'manager', 'team_type').prefetch_related('members')
    if query:
        from django.db.models import Q
        teams = teams.filter(
            Q(team_name__icontains=query) |
            Q(team_purpose__icontains=query) |
            Q(manager__first_name__icontains=query) |
            Q(manager__last_name__icontains=query)
        )
    if dept_filter:
        teams = teams.filter(department__id=dept_filter)
    if status_filter:
        teams = teams.filter(status=status_filter)
    departments = Department.objects.all()
    return render(request, 'teams/team_list.html', {
        'teams': teams, 'query': query,
        'departments': departments,
        'dept_filter': dept_filter,
        'status_filter': status_filter,
    })


@login_required
def team_detail(request, pk):
    team = get_object_or_404(Team, pk=pk)
    members = TeamMember.objects.filter(team=team).select_related('user')
    upstream = TeamDependency.objects.filter(team=team, dependency_type='upstream').select_related('depends_on')
    downstream = TeamDependency.objects.filter(team=team, dependency_type='downstream').select_related('depends_on')
    repos = CodeRepository.objects.filter(team=team)
    channels = ContactChannel.objects.filter(team=team)
    from scheduling.models import Meeting
    from django.utils import timezone
    upcoming_meetings = Meeting.objects.filter(team=team, date_time__gte=timezone.now()).order_by('date_time')[:3]
    return render(request, 'teams/team_detail.html', {
        'team': team, 'members': members,
        'upstream': upstream, 'downstream': downstream,
        'repos': repos, 'channels': channels,
        'upcoming_meetings': upcoming_meetings,
    })


@login_required
def email_team(request, pk):
    team = get_object_or_404(Team, pk=pk)
    if request.method == 'POST':
        form = TeamEmailForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            recipient = team.team_contactemail or 'noreply@broadcast.com'
            send_mail(
                subject=f"[BET Portal] {subject}",
                message=f"From: {request.user.get_full_name()} ({request.user.email})\n\n{body}",
                from_email='portal@broadcast.com',
                recipient_list=[recipient],
                fail_silently=True,
            )
            AuditLog.objects.create(
                user=request.user, action_type='insert',
                table_name='Email', description=f"Email sent to team '{team.team_name}'"
            )
            messages.success(request, f'Email sent to {team.team_name}. (Check console in dev mode)')
            return redirect('team_detail', pk=pk)
    else:
        form = TeamEmailForm()
    return render(request, 'teams/email_team.html', {'team': team, 'form': form})


@login_required
def schedule_team_meeting(request, pk):
    """Schedule a meeting directly from the team page"""
    team = get_object_or_404(Team, pk=pk)
    return redirect(f'/schedule/new/?team={pk}')


@login_required
def dependencies_view(request, pk):
    team = get_object_or_404(Team, pk=pk)
    upstream = TeamDependency.objects.filter(team=team, dependency_type='upstream').select_related('depends_on')
    downstream = TeamDependency.objects.filter(team=team, dependency_type='downstream').select_related('depends_on')
    all_teams = Team.objects.exclude(pk=pk)
    return render(request, 'teams/dependencies.html', {
        'team': team, 'upstream': upstream,
        'downstream': downstream, 'all_teams': all_teams,
    })
