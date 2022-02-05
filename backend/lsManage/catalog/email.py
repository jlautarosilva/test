from tokenize import String, group
from typing import List
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User

#Function to send an e-mail to all the users in the admin group
def emailAdmins(message):
    emails = User.objects.filter(groups__name="admin").exclude(email="").values_list("email", flat=True)
    admins = list(emails)
    send_mail(
        subject="OUR PRODUCTS ARE MUTATING!!!",
        message=message,
        from_email="jlautarosilva@gmail.com",
        recipient_list=admins)