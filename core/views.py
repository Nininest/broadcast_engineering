from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from teams.models import Team
from organization.models import Department
from core.models import AuditLog, Notification
from django.contrib.auth.models import User

# Create your views here.

@login_required
def dashboard_view(request):
    total_teams = Team.objects.count()
    active_teams = Team.objects.filter(status='active').count()
    disbanded_teams = Team.objects.filter(status='disbanded').count()
    total_departments = Department.objects.count()
    total_engineers = User.objects.count()
    teams_no_manager = Team.objects.filter(manager__isnull=True).count()
    recent_teams = Team.objects.select_related('department').order_by('-updated_at')[:5]
    recent_logs = AuditLog.objects.select_related('user').order_by('-timestamp')[:6]
    dept_stats = Department.objects.annotate(tc=Count('teams')).order_by('-tc')[:5]
    unread_notifications = Notification.objects.filter(user=request.user, read=False).count()

    return render(request, 'core/dashboard.html',{
        'total_teams':total_teams, 
        'active_teams':active_teams,
        'disbanded_teams':disbanded_teams,
        'total_departments': total_departments, 
        'total_engineers': total_engineers,
        'teams_no_manager':teams_no_manager, 
        'recent_teams':recent_teams, 
        'recent_logs':recent_logs, 
        'dept_stats':dept_stats, 
        'unread_notifications':unread_notifications,
    })

@login_required
def notifications_views(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    Notification.objects.filter(user=request.user, read=False).update(read=True)
    return render(request, 'core/notifications.html', {'notifications':notifications})
