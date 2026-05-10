# import_data.py
# Place this file in your project ROOT (same folder as manage.py)
# Run with:  python manage.py shell < import_data.py

from organization.models import Department, TeamType
from teams.models import Team, TeamMember, CodeRepository, ContactChannel, TeamDependency
from django.contrib.auth.models import User

print("=" * 55)
print("  Broadcast Engineering — Organization Data Import")
print("=" * 55)

# ══════════════════════════════════════════════════════════
# STEP 1 — Department Heads (Users)
# ══════════════════════════════════════════════════════════
print("\n── Step 1: Department Heads ────────────────────────────")

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
    print(f"  {'✅ Created' if created else '— Exists '} user: {user.get_full_name()}")


# ══════════════════════════════════════════════════════════
# STEP 2 — Departments
# NOTE: field is department_name (NOT name) and
#       department_head (NOT head) — matches organization/models.py
# ══════════════════════════════════════════════════════════
print("\n── Step 2: Departments ─────────────────────────────────")

departments = [
    {
        'department_name': 'xTV_Web',
        'department_specialisation': 'Web TV platform engineering — CI/CD, security, DevOps, frontend',
        'head_username': 'sebastian.holt',
    },
    {
        'department_name': 'Native TVs',
        'department_specialisation': 'Native TV apps — Roku, Apple TV; agile delivery and patch management',
        'head_username': 'mason.briggs',
    },
    {
        'department_name': 'Mobile',
        'department_specialisation': 'Mobile client engineering — caching, versioning, UI performance',
        'head_username': 'violet.ramsey',
    },
    {
        'department_name': 'Reliability_Tool',
        'department_specialisation': 'SRE, tooling, UX, serverless functions, and hackathon facilitation',
        'head_username': 'lucy.vaughn',
    },
    {
        'department_name': 'Arch',
        'department_specialisation': 'System architecture — microservices, API gateways, SDK development',
        'head_username': 'theodore.knox',
    },
    {
        'department_name': 'Programme',
        'department_specialisation': 'Programme management — high-performance and quantum computing',
        'head_username': 'bella.monroe',
    },
]

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
        # update head and specialisation if missing
        updated = False
        if head and dept.department_head != head:
            dept.department_head = head
            updated = True
        if not dept.department_specialisation:
            dept.department_specialisation = d['department_specialisation']
            updated = True
        if updated:
            dept.save()
    print(f"  {'✅ Created' if created else '— Exists '} department: {dept.department_name}  |  Head: {head.get_full_name() if head else 'none'}")


# ══════════════════════════════════════════════════════════
# STEP 3 — TeamTypes
# NOTE: field is name — matches organization/models.py
# ══════════════════════════════════════════════════════════
print("\n── Step 3: Team Types ──────────────────────────────────")

team_types = [
    ('Engineering',     'General software engineering team'),
    ('DevOps',          'CI/CD pipelines, infrastructure as code, and cloud automation'),
    ('Agile Coaching',  'Scrum mastery, SAFe, Kanban coaching, and agile transformation'),
    ('Security',        'Cybersecurity, encryption, authentication, and compliance'),
    ('Data',            'Big data, ETL pipelines, real-time streaming, and analytics'),
    ('Frontend',        'UI/UX design, component libraries, and web performance'),
    ('QA / Testing',    'Quality assurance, test automation, and reliability engineering'),
    ('Architecture',    'System design, microservices, API gateways, and SDK development'),
    ('Scrum',           'Teams practicing Scrum methodology'),
    ('Kanban',          'Teams practicing Kanban methodology'),
    ('SAFe',            'Teams following Scaled Agile Framework'),
]

for name, description in team_types:
    tt, created = TeamType.objects.get_or_create(
        name=name,
        defaults={'description': description}
    )
    print(f"  {'✅ Created' if created else '— Exists '} team type: {tt.name}")


# ══════════════════════════════════════════════════════════
# STEP 4 — Team Leaders (Users)
# ══════════════════════════════════════════════════════════
print("\n── Step 4: Team Leaders ────────────────────────────────")

leaders = [
    # xTV_Web
    {'username': 'olivia.carter',     'first_name': 'Olivia',    'last_name': 'Carter'},
    {'username': 'james.bennett',     'first_name': 'James',     'last_name': 'Bennett'},
    {'username': 'emma.richardson',   'first_name': 'Emma',      'last_name': 'Richardson'},
    {'username': 'benjamin.hayes',    'first_name': 'Benjamin',  'last_name': 'Hayes'},
    {'username': 'sophia.mitchell',   'first_name': 'Sophia',    'last_name': 'Mitchell'},
    {'username': 'william.cooper',    'first_name': 'William',   'last_name': 'Cooper'},
    {'username': 'isabella.ross',     'first_name': 'Isabella',  'last_name': 'Ross'},
    {'username': 'elijah.parker',     'first_name': 'Elijah',    'last_name': 'Parker'},
    {'username': 'ava.sullivan',      'first_name': 'Ava',       'last_name': 'Sullivan'},
    {'username': 'noah.campbell',     'first_name': 'Noah',      'last_name': 'Campbell'},
    # xTV_Web (under Nora Chandler dept head)
    {'username': 'mia.henderson',     'first_name': 'Mia',       'last_name': 'Henderson'},
    {'username': 'lucas.foster',      'first_name': 'Lucas',     'last_name': 'Foster'},
    {'username': 'charlotte.murphy',  'first_name': 'Charlotte', 'last_name': 'Murphy'},
    {'username': 'henry.ward',        'first_name': 'Henry',     'last_name': 'Ward'},
    {'username': 'amelia.brooks',     'first_name': 'Amelia',    'last_name': 'Brooks'},
    # Native TVs
    {'username': 'alexander.perry',   'first_name': 'Alexander', 'last_name': 'Perry'},
    {'username': 'evelyn.hughes',     'first_name': 'Evelyn',    'last_name': 'Hughes'},
    {'username': 'daniel.scott',      'first_name': 'Daniel',    'last_name': 'Scott'},
    {'username': 'harper.lewis',      'first_name': 'Harper',    'last_name': 'Lewis'},
    {'username': 'matthew.reed',      'first_name': 'Matthew',   'last_name': 'Reed'},
    {'username': 'scarlett.edwards',  'first_name': 'Scarlett',  'last_name': 'Edwards'},
    {'username': 'jack.turner',       'first_name': 'Jack',      'last_name': 'Turner'},
    {'username': 'lily.phillips',     'first_name': 'Lily',      'last_name': 'Phillips'},
    {'username': 'samuel.morgan',     'first_name': 'Samuel',    'last_name': 'Morgan'},
    {'username': 'grace.patterson',   'first_name': 'Grace',     'last_name': 'Patterson'},
    # Mobile
    {'username': 'owen.barnes',       'first_name': 'Owen',      'last_name': 'Barnes'},
    {'username': 'chloe.hall',        'first_name': 'Chloe',     'last_name': 'Hall'},
    {'username': 'nathan.fisher',     'first_name': 'Nathan',    'last_name': 'Fisher'},
    {'username': 'zoey.stevens',      'first_name': 'Zoey',      'last_name': 'Stevens'},
    {'username': 'caleb.bryant',      'first_name': 'Caleb',     'last_name': 'Bryant'},
    {'username': 'hannah.simmons',    'first_name': 'Hannah',    'last_name': 'Simmons'},
    {'username': 'isaac.jenkins',     'first_name': 'Isaac',     'last_name': 'Jenkins'},
    {'username': 'madison.clarke',    'first_name': 'Madison',   'last_name': 'Clarke'},
    {'username': 'gabriel.coleman',   'first_name': 'Gabriel',   'last_name': 'Coleman'},
    {'username': 'riley.sanders',     'first_name': 'Riley',     'last_name': 'Sanders'},
    {'username': 'leo.watson',        'first_name': 'Leo',       'last_name': 'Watson'},
    {'username': 'victoria.price',    'first_name': 'Victoria',  'last_name': 'Price'},
    {'username': 'julian.bell',       'first_name': 'Julian',    'last_name': 'Bell'},
    # Reliability_Tool
    {'username': 'layla.russell',     'first_name': 'Layla',     'last_name': 'Russell'},
    {'username': 'ethan.griffin',     'first_name': 'Ethan',     'last_name': 'Griffin'},
    {'username': 'aurora.cooper',     'first_name': 'Aurora',    'last_name': 'Cooper'},
    {'username': 'dylan.spencer',     'first_name': 'Dylan',     'last_name': 'Spencer'},
    {'username': 'stella.martinez',   'first_name': 'Stella',    'last_name': 'Martinez'},
    # Arch
    {'username': 'levi.bishop',       'first_name': 'Levi',      'last_name': 'Bishop'},
    {'username': 'eleanor.freeman',   'first_name': 'Eleanor',   'last_name': 'Freeman'},
    # Programme
    {'username': 'hudson.ford',       'first_name': 'Hudson',    'last_name': 'Ford'},
]

for l in leaders:
    user, created = User.objects.get_or_create(
        username=l['username'],
        defaults={
            'first_name': l['first_name'],
            'last_name':  l['last_name'],
            'email': f"{l['username']}@broadcast.com",
        }
    )
    if created:
        user.set_password('Test1234!')
        user.save()
    print(f"  {'✅ Created' if created else '— Exists '} user: {user.get_full_name()}")


# ══════════════════════════════════════════════════════════
# STEP 5 — Teams
# NOTE: field is team_name (NOT name) — matches teams/models.py
# ══════════════════════════════════════════════════════════
print("\n── Step 5: Teams ───────────────────────────────────────")

eng_type  = TeamType.objects.get(name='Engineering')
agile_type = TeamType.objects.get(name='Agile Coaching')
devops_type = TeamType.objects.get(name='DevOps')
sec_type  = TeamType.objects.get(name='Security')
data_type = TeamType.objects.get(name='Data')
fe_type   = TeamType.objects.get(name='Frontend')
qa_type   = TeamType.objects.get(name='QA / Testing')
arch_type = TeamType.objects.get(name='Architecture')

teams_data = [
    # ── xTV_Web ──────────────────────────────────────────
    {'team_name': 'Code Warriors',          'dept': 'xTV_Web',          'manager': 'olivia.carter',    'type': devops_type,  'purpose': 'Infrastructure scalability, CI/CD integration, platform resilience'},
    {'team_name': 'The Debuggers',          'dept': 'xTV_Web',          'manager': 'james.bennett',    'type': eng_type,     'purpose': 'Advanced debugging tools, automated error detection, root cause analysis'},
    {'team_name': 'Bit Masters',            'dept': 'xTV_Web',          'manager': 'emma.richardson',  'type': sec_type,     'purpose': 'Security compliance, encryption techniques, data integrity'},
    {'team_name': 'Agile Avengers',         'dept': 'xTV_Web',          'manager': 'benjamin.hayes',   'type': agile_type,   'purpose': 'Agile transformation, workflow optimization, lean process improvement'},
    {'team_name': 'Syntax Squad',           'dept': 'xTV_Web',          'manager': 'sophia.mitchell',  'type': devops_type,  'purpose': 'Automated deployment pipelines, release management, rollback strategies'},
    {'team_name': 'The Codebreakers',       'dept': 'xTV_Web',          'manager': 'william.cooper',   'type': sec_type,     'purpose': 'Cryptographic security, authentication protocols, secure APIs'},
    {'team_name': 'DevOps Dynasty',         'dept': 'xTV_Web',          'manager': 'isabella.ross',    'type': devops_type,  'purpose': 'DevOps best practices, Kubernetes orchestration, cloud automation'},
    {'team_name': 'Byte Force',             'dept': 'xTV_Web',          'manager': 'elijah.parker',    'type': eng_type,     'purpose': 'Cloud infrastructure, API gateway development, serverless architecture'},
    {'team_name': 'The Cloud Architects',   'dept': 'xTV_Web',          'manager': 'ava.sullivan',     'type': arch_type,    'purpose': 'Cloud-native applications, distributed systems, multi-region deployments'},
    {'team_name': 'Full Stack Ninjas',      'dept': 'xTV_Web',          'manager': 'noah.campbell',    'type': eng_type,     'purpose': 'Frontend and backend synchronization, API integration, UX/UI consistency'},
    {'team_name': 'The Error Handlers',     'dept': 'xTV_Web',          'manager': 'mia.henderson',    'type': eng_type,     'purpose': 'Log aggregation, AI-driven anomaly detection, real-time monitoring'},
    {'team_name': 'Stack Overflow Survivors','dept': 'xTV_Web',         'manager': 'lucas.foster',     'type': eng_type,     'purpose': 'Knowledge management, engineering playbooks, documentation automation'},
    {'team_name': 'The Binary Beasts',      'dept': 'xTV_Web',          'manager': 'charlotte.murphy', 'type': eng_type,     'purpose': 'High-performance computing, low-latency data processing, algorithm efficiency'},
    {'team_name': 'API Avengers',           'dept': 'xTV_Web',          'manager': 'henry.ward',       'type': arch_type,    'purpose': 'API security, authentication layers, API scalability'},
    {'team_name': 'The Algorithm Alliance', 'dept': 'xTV_Web',          'manager': 'amelia.brooks',    'type': data_type,    'purpose': 'Machine learning models, AI-driven analytics, data science applications'},
    # ── Native TVs ───────────────────────────────────────
    {'team_name': 'Data Wranglers',         'dept': 'Native TVs',       'manager': 'alexander.perry',  'type': data_type,    'purpose': 'Big data engineering, real-time data streaming, database optimization'},
    {'team_name': 'The Sprint Kings',       'dept': 'Native TVs',       'manager': 'evelyn.hughes',    'type': agile_type,   'purpose': 'Agile backlog management, sprint retrospectives, delivery forecasting'},
    {'team_name': 'Exception Catchers',     'dept': 'Native TVs',       'manager': 'daniel.scott',     'type': eng_type,     'purpose': 'Fault tolerance, system resilience, disaster recovery planning'},
    {'team_name': 'Code Monkeys',           'dept': 'Native TVs',       'manager': 'harper.lewis',     'type': devops_type,  'purpose': 'Patch deployment, rollback automation, version control best practices'},
    {'team_name': 'The Compile Crew',       'dept': 'Native TVs',       'manager': 'matthew.reed',     'type': eng_type,     'purpose': 'Compiler optimization, static code analysis, build system improvements'},
    {'team_name': 'Git Good',               'dept': 'Native TVs',       'manager': 'scarlett.edwards', 'type': devops_type,  'purpose': 'Branching strategies, merge conflict resolution, Git best practices'},
    {'team_name': 'The CI/CD Squad',        'dept': 'Native TVs',       'manager': 'jack.turner',      'type': devops_type,  'purpose': 'Continuous integration, automated testing, deployment pipelines'},
    {'team_name': 'Bug Exterminators',      'dept': 'Native TVs',       'manager': 'lily.phillips',    'type': qa_type,      'purpose': 'Performance profiling, automated test generation, security patching'},
    {'team_name': 'The Agile Alchemists',   'dept': 'Native TVs',       'manager': 'samuel.morgan',    'type': agile_type,   'purpose': 'Agile maturity assessments, coaching and mentorship, SAFe/LeSS frameworks'},
    {'team_name': 'The Hotfix Heroes',      'dept': 'Native TVs',       'manager': 'grace.patterson',  'type': eng_type,     'purpose': 'Emergency response, rollback strategies, live system debugging'},
    # ── Mobile ───────────────────────────────────────────
    {'team_name': 'Cache Me Outside',       'dept': 'Mobile',           'manager': 'owen.barnes',      'type': eng_type,     'purpose': 'Caching strategies, distributed cache systems, database query optimization'},
    {'team_name': 'The Scrum Lords',        'dept': 'Mobile',           'manager': 'chloe.hall',       'type': agile_type,   'purpose': 'Agile training, sprint planning automation, process governance'},
    {'team_name': 'The 404 Not Found',      'dept': 'Mobile',           'manager': 'nathan.fisher',    'type': eng_type,     'purpose': 'Error page personalization, debugging-as-a-service, incident response'},
    {'team_name': 'The Version Controllers','dept': 'Mobile',           'manager': 'zoey.stevens',     'type': devops_type,  'purpose': 'GitOps workflows, repository security, automated versioning'},
    {'team_name': 'DevNull Pioneers',       'dept': 'Mobile',           'manager': 'caleb.bryant',     'type': eng_type,     'purpose': 'Logging frameworks, observability enhancements, error handling APIs'},
    {'team_name': 'The Code Refactors',     'dept': 'Mobile',           'manager': 'hannah.simmons',   'type': eng_type,     'purpose': 'Code maintainability, tech debt reduction, automated refactoring tools'},
    {'team_name': 'The Jenkins Juggernauts','dept': 'Mobile',           'manager': 'isaac.jenkins',    'type': devops_type,  'purpose': 'CI/CD pipeline optimization, Jenkins plugin development, infrastructure as code'},
    {'team_name': 'Infinite Loopers',       'dept': 'Mobile',           'manager': 'madison.clarke',   'type': fe_type,      'purpose': 'Frontend performance optimization, UI/UX consistency, component reusability'},
    {'team_name': 'The Feature Crafters',   'dept': 'Mobile',           'manager': 'gabriel.coleman',  'type': fe_type,      'purpose': 'Feature flagging, A/B testing automation, rapid prototyping'},
    {'team_name': 'The Bit Manipulators',   'dept': 'Mobile',           'manager': 'riley.sanders',    'type': eng_type,     'purpose': 'Binary data processing, encoding/decoding algorithms, compression techniques'},
    {'team_name': 'Kernel Crushers',        'dept': 'Mobile',           'manager': 'leo.watson',       'type': eng_type,     'purpose': 'Low-level optimization, OS kernel tuning, hardware acceleration'},
    {'team_name': 'The Git Masters',        'dept': 'Mobile',           'manager': 'victoria.price',   'type': devops_type,  'purpose': 'Git automation, monorepo strategies, repository analytics'},
    {'team_name': 'The API Explorers',      'dept': 'Mobile',           'manager': 'julian.bell',      'type': arch_type,    'purpose': 'API documentation, API analytics, developer experience optimization'},
    # ── Reliability_Tool ─────────────────────────────────
    {'team_name': 'The Lambda Legends',     'dept': 'Reliability_Tool', 'manager': 'layla.russell',    'type': eng_type,     'purpose': 'Serverless architecture, event-driven development, microservice automation'},
    {'team_name': 'The Encryption Squad',   'dept': 'Reliability_Tool', 'manager': 'ethan.griffin',    'type': sec_type,     'purpose': 'Cybersecurity research, cryptographic key management, secure data storage'},
    {'team_name': 'The UX Wizards',         'dept': 'Reliability_Tool', 'manager': 'aurora.cooper',    'type': fe_type,      'purpose': 'Accessibility, user behavior analytics, UI/UX best practices'},
    {'team_name': 'The Hackathon Hustlers', 'dept': 'Reliability_Tool', 'manager': 'dylan.spencer',    'type': eng_type,     'purpose': 'Rapid prototyping, proof-of-concept development, hackathon facilitation'},
    {'team_name': 'The Frontend Phantoms',  'dept': 'Reliability_Tool', 'manager': 'stella.martinez',  'type': fe_type,      'purpose': 'Frontend frameworks, web performance tuning, component libraries'},
    # ── Arch ─────────────────────────────────────────────
    {'team_name': 'The Dev Dragons',        'dept': 'Arch',             'manager': 'levi.bishop',      'type': arch_type,    'purpose': 'API integrations, SDK development, plugin architecture'},
    {'team_name': 'The Microservice Mavericks','dept': 'Arch',          'manager': 'eleanor.freeman',  'type': arch_type,    'purpose': 'Microservice governance, inter-service communication, API gateways'},
    # ── Programme ────────────────────────────────────────
    {'team_name': 'The Quantum Coders',     'dept': 'Programme',        'manager': 'hudson.ford',      'type': eng_type,     'purpose': 'Quantum computing simulations, parallel processing, AI-assisted coding'},
]

for t in teams_data:
    try:
        dept    = Department.objects.get(department_name=t['dept'])
        manager = User.objects.get(username=t['manager'])
        team, created = Team.objects.get_or_create(
            team_name=t['team_name'],
            defaults={
                'department':   dept,
                'manager':      manager,
                'team_type':    t['type'],
                'team_purpose': t['purpose'],
                'status':       'active',
            }
        )
        if not created:
            team.department = dept
            team.manager    = manager
            team.team_type  = t['type']
            team.save()
        print(f"  {'✅ Created' if created else '🔄 Updated'} team: {team.team_name}  ({t['dept']})")
    except Department.DoesNotExist:
        print(f"  ❌ ERROR — Department not found: '{t['dept']}'")
    except User.DoesNotExist:
        print(f"  ❌ ERROR — User not found: '{t['manager']}'")


# ══════════════════════════════════════════════════════════
# STEP 6 — Team Dependencies
# ══════════════════════════════════════════════════════════
print("\n── Step 6: Team Dependencies ───────────────────────────")

dependencies = [
    # (team_name,                    depends_on_name,            type)
    ('Code Warriors',               'The Debuggers',            'downstream'),
    ('The Debuggers',               'Bit Masters',              'downstream'),
    ('Bit Masters',                 'API Avengers',             'downstream'),
    ('Agile Avengers',              'The Sprint Kings',         'downstream'),
    ('Syntax Squad',                'The Feature Crafters',     'downstream'),
    ('DevOps Dynasty',              'Code Warriors',            'downstream'),
    ('Byte Force',                  'API Avengers',             'downstream'),
    ('The Cloud Architects',        'Byte Force',               'downstream'),
    ('The Cloud Architects',        'Cache Me Outside',         'downstream'),
    ('Full Stack Ninjas',           'The API Explorers',        'downstream'),
    ('The Error Handlers',          'The Debuggers',            'downstream'),
    ('Stack Overflow Survivors',    'The Scrum Lords',          'downstream'),
    ('The Binary Beasts',           'The Algorithm Alliance',   'downstream'),
    ('API Avengers',                'The Dev Dragons',          'downstream'),
    ('The Algorithm Alliance',      'The Codebreakers',         'downstream'),
    ('Data Wranglers',              'The Bit Manipulators',     'downstream'),
    ('The Sprint Kings',            'The Agile Alchemists',     'downstream'),
    ('Exception Catchers',          'The Debuggers',            'downstream'),
    ('Code Monkeys',                'The Version Controllers',  'downstream'),
    ('The Compile Crew',            'The Bit Manipulators',     'downstream'),
    ('Git Good',                    'The Version Controllers',  'downstream'),
    ('The CI/CD Squad',             'Syntax Squad',             'downstream'),
    ('Bug Exterminators',           'The Debuggers',            'downstream'),
    ('The Agile Alchemists',        'Stack Overflow Survivors', 'downstream'),
    ('The Hotfix Heroes',           'The CI/CD Squad',          'downstream'),
    ('The Hotfix Heroes',           'Code Monkeys',             'downstream'),
    ('The Scrum Lords',             'The Sprint Kings',         'downstream'),
    ('The Scrum Lords',             'Agile Avengers',           'downstream'),
    ('The Version Controllers',     'The Compile Crew',         'downstream'),
    ('The Version Controllers',     'The 404 Not Found',        'downstream'),
    ('DevNull Pioneers',            'The API Explorers',        'downstream'),
    ('The Jenkins Juggernauts',     'DevOps Dynasty',           'downstream'),
    ('The Jenkins Juggernauts',     'Git Good',                 'downstream'),
    ('The Feature Crafters',        'The Error Handlers',       'downstream'),
    ('The Feature Crafters',        'Syntax Squad',             'downstream'),
    ('The UX Wizards',              'Full Stack Ninjas',        'downstream'),
    ('The UX Wizards',              'The Feature Crafters',     'downstream'),
    ('The Lambda Legends',          'API Avengers',             'downstream'),
    ('The Encryption Squad',        'API Avengers',             'downstream'),
    ('The Encryption Squad',        'The API Explorers',        'downstream'),
    ('The Microservice Mavericks',  'The Code Refactors',       'downstream'),
    ('The Microservice Mavericks',  'The Lambda Legends',       'downstream'),
]

dep_created = 0
dep_skipped = 0
for team_name, depends_on_name, dep_type in dependencies:
    try:
        team       = Team.objects.get(team_name=team_name)
        depends_on = Team.objects.get(team_name=depends_on_name)
        _, created = TeamDependency.objects.get_or_create(
            team=team,
            depends_on=depends_on,
            defaults={'dependency_type': dep_type}
        )
        if created:
            dep_created += 1
            print(f"  ✅ Linked: {team_name} → {depends_on_name}")
        else:
            dep_skipped += 1
    except Team.DoesNotExist as e:
        print(f"  ❌ ERROR — Team not found: {e}")


# ══════════════════════════════════════════════════════════
# SUMMARY
# ══════════════════════════════════════════════════════════
print("\n" + "=" * 55)
print("✅  Import Complete!")
print(f"   Departments : {Department.objects.count()}")
print(f"   TeamTypes   : {TeamType.objects.count()}")
print(f"   Teams       : {Team.objects.count()}")
print(f"   Users       : {User.objects.count()}")
print(f"   Dependencies: {TeamDependency.objects.count()}")
print("=" * 55)