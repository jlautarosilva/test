from tokenize import String, group
from typing import List
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

def emailAdmins(message):
    emails = User.objects.filter(groups__name="admin").exclude(email="").values_list("email", flat=True)
    admins = list(emails)
    send_mail(
        subject="OUR PRODUCTS ARE MUTATING!!!",
        message=message,
        from_email="test@test.cl",
        recipient_list=admins)