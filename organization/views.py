"""Organization App - Sushma
Departments, TeamType, Dependencies, Org Chart
"""
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from organization.models import Department, TeamType
from teams.models import Team, TeamDependency


@login_required
def department_list(request):
    departments = Department.objects.prefetch_related('teams').all()
    team_types = TeamType.objects.all()
    return render(request, 'organization/department_list.html', {
        'departments': departments, 'team_types': team_types
    })


@login_required
def department_detail(request, pk):
    dept = get_object_or_404(Department, pk=pk)
    teams = Team.objects.filter(department=dept).prefetch_related('members', 'team_type')
    return render(request, 'organization/department_detail.html', {'dept': dept, 'teams': teams})


@login_required
def teamtype_detail(request, pk):
    team_type = get_object_or_404(TeamType, pk=pk)
    teams = Team.objects.filter(team_type=team_type)
    return render(request, 'organization/teamtype_detail.html', {'team_type': team_type, 'teams': teams})


@login_required
def org_chart(request):
    departments = Department.objects.prefetch_related('teams__members', 'teams__team_type').all()
    return render(request, 'organization/org_chart.html', {'departments': departments})


@login_required
def dependency_graph(request):
    teams = Team.objects.all()
    dependencies = TeamDependency.objects.select_related('team', 'depends_on').all()
    return render(request, 'organization/dependency_graph.html', {
        'teams': teams, 'dependencies': dependencies,
    })

