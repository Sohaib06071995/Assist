import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','OnlineMonetoringSystem.settings')

import django
django.setup()

## FAKE POP  SCRIPT
import random
from Activity.models import *
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_Active_Description = fakegen.name()
        fake_Exceting_Agency = fakegen.company()
        fake_Assigned_By = fakegen.name()
        fake_Deadline = fakegen.date()
        fake_Action_Required = fakegen.name()

        p_a = Pending_Activity.objects.get_or_create(Active_Description=fake_Active_Description,Exceting_Agency=fake_Exceting_Agency,Assigned_By=fake_Assigned_By,Deadline=fake_Deadline,Action_Required=fake_Action_Required)[0]
print("populating scripts")
populate(20)
print("populating complete")
