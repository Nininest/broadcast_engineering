"""
Management command: import_organization
Place this file at:
  organization/management/commands/import_organization.py

Run with:
  python manage.py import_organization

This script hardcodes all data from the Excel sheet directly —
no Excel file needed at runtime.

Populates:
  - organization.Department  (6 departments)
  - organization.TeamType    (11 team types)
  - Django User              (department heads only)
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from organization.models import Department, TeamType


class Command(BaseCommand):
    help = "Populate Departments and TeamTypes for the organization app."

    def handle(self, *args, **options):

        # ══════════════════════════════════════════════════════
        # STEP 1 — Department Head Users
        # ══════════════════════════════════════════════════════
        self.stdout.write("\n── Step 1: Department Head Users ───────────────────")

        dept_heads = [
            {'username': 'sebastian.holt',  'first_name': 'Sebastian', 'last_name': 'Holt'},
            {'username': 'nora.chandler',   'first_name': 'Nora',      'last_name': 'Chandler'},
            {'username': 'mason.briggs',    'first_name': 'Mason',     'last_name': 'Briggs'},
            {'username': 'violet.ramsey',   'first_name': 'Violet',    'last_name': 'Ramsey'},
            {'username': 'adam.sinclair',   'first_name': 'Adam',      'last_name': 'Sinclair'},
            {'username': 'lucy.vaughn',     'first_name': 'Lucy',      'last_name': 'Vaughn'},
            {'username': 'theodore.knox',   'first_name': 'Theodore',  'last_name': 'Knox'},
            {'username': 'bella.monroe',    'first_name': 'Bella',     'last_name': 'Monroe'},
        ]

        for h in dept_heads:
            user, created = User.objects.get_or_create(
                username=h['username'],
                defaults={
                    'first_name': h['first_name'],
                    'last_name':  h['last_name'],
                    'email': f"{h['username']}@broadcast.com",
                }
            )
            if created:
                user.set_password('Test1234!')
                user.save()
            status = "✅ Created" if created else "— Exists "
            self.stdout.write(f"  {status}  {user.get_full_name()}")

        # ══════════════════════════════════════════════════════
        # STEP 2 — Departments
        # Field names from organization/models.py:
        #   department_name           (CharField)
        #   department_specialisation (TextField)
        #   department_head           (ForeignKey -> User)
        # ══════════════════════════════════════════════════════
        self.stdout.write("\n── Step 2: Departments ─────────────────────────────")

        departments = [
            {
                'department_name': 'xTV_Web',
                'department_specialisation': (
                    'Web TV platform engineering — CI/CD integration, '
                    'infrastructure scalability, security compliance, '
                    'DevOps practices, and frontend development.'
                ),
                'head_username': 'sebastian.holt',
            },
            {
                'department_name': 'Native TVs',
                'department_specialisation': (
                    'Native TV application engineering — Roku and Apple TV '
                    'clients; agile delivery, patch management, and '
                    'build system optimisation.'
                ),
                'head_username': 'mason.briggs',
            },
            {
                'department_name': 'Mobile',
                'department_specialisation': (
                    'Mobile client engineering — caching strategies, '
                    'GitOps versioning, UI performance, feature flagging, '
                    'and low-level optimisation.'
                ),
                'head_username': 'violet.ramsey',
            },
            {
                'department_name': 'Reliability_Tool',
                'department_specialisation': (
                    'Site reliability engineering and tooling — serverless '
                    'functions, UX design, cryptographic security, '
                    'and rapid prototyping.'
                ),
                'head_username': 'lucy.vaughn',
            },
            {
                'department_name': 'Arch',
                'department_specialisation': (
                    'System architecture — microservice governance, '
                    'API gateway design, SDK development, '
                    'and inter-service communication.'
                ),
                'head_username': 'theodore.knox',
            },
            {
                'department_name': 'Programme',
                'department_specialisation': (
                    'Programme management — high-performance computing, '
                    'quantum computing simulations, and AI-assisted coding.'
                ),
                'head_username': 'bella.monroe',
            },
        ]

        dept_created = 0
        dept_updated = 0

        for d in departments:
            head = User.objects.filter(username=d['head_username']).first()

            dept, created = Department.objects.get_or_create(
                department_name=d['department_name'],
                defaults={
                    'department_specialisation': d['department_specialisation'],
                    'department_head': head,
                }
            )

            if not created:
                changed = False
                if not dept.department_specialisation:
                    dept.department_specialisation = d['department_specialisation']
                    changed = True
                if head and dept.department_head != head:
                    dept.department_head = head
                    changed = True
                if changed:
                    dept.save()
                    dept_updated += 1
            else:
                dept_created += 1

            status = "✅ Created" if created else "— Exists "
            head_name = head.get_full_name() if head else "no head"
            self.stdout.write(
                f"  {status}  {dept.department_name:<20}  Head: {head_name}"
            )

        # ══════════════════════════════════════════════════════
        # STEP 3 — TeamTypes
        # Field names from organization/models.py:
        #   name         (CharField)
        #   description  (TextField)
        # ══════════════════════════════════════════════════════
        self.stdout.write("\n── Step 3: Team Types ──────────────────────────────")

        team_types = [
            ('Engineering',    'General software engineering — backend, APIs, and system development.'),
            ('DevOps',         'CI/CD pipelines, infrastructure as code, Kubernetes, and cloud automation.'),
            ('Agile Coaching', 'Scrum mastery, SAFe, Kanban coaching, and agile transformation.'),
            ('Security',       'Cybersecurity, encryption, authentication protocols, and compliance.'),
            ('Data',           'Big data engineering, ETL pipelines, real-time streaming, and analytics.'),
            ('Frontend',       'UI/UX design, component libraries, web performance, and accessibility.'),
            ('QA / Testing',   'Quality assurance, test automation, load testing, and reliability.'),
            ('Architecture',   'System design, microservices, API gateways, and SDK development.'),
            ('Scrum',          'Teams following the Scrum framework for sprint-based delivery.'),
            ('Kanban',         'Teams using Kanban for continuous flow and work-in-progress limits.'),
            ('SAFe',           'Teams aligned to the Scaled Agile Framework for large-scale delivery.'),
        ]

        type_created = 0

        for name, description in team_types:
            tt, created = TeamType.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
            if created:
                type_created += 1
            status = "✅ Created" if created else "— Exists "
            self.stdout.write(f"  {status}  {tt.name}")

        # ══════════════════════════════════════════════════════
        # SUMMARY
        # ══════════════════════════════════════════════════════
        self.stdout.write(self.style.SUCCESS(
            f"\n✅ import_organization complete:\n"
            f"   Departments created : {dept_created}\n"
            f"   Departments updated : {dept_updated}\n"
            f"   TeamTypes created   : {type_created}\n"
            f"\n   Total Departments   : {Department.objects.count()}\n"
            f"   Total TeamTypes     : {TeamType.objects.count()}\n"
        ))