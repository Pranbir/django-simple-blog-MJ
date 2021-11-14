from celery import shared_task
from django.core.mail import send_mail
import time


@shared_task
def bekar(n):
    print("I am executing")
    for i in range(n):
        time.sleep(4)
        print("I am still sleeping.. Count : {}".format(i))
    print("I wake up.... :) ")
    return "Value of n is : {}".format(n)


@shared_task
def mail(body, name, email):
    send_mail(
    'Django Contact Form Data',
    """
    contact form data : 
    name : {}
    email : {}
    message : {}
    """.format(name,email,body),
    'enterprize@skill-edge.com',
    ['pranbirsarkar@gmail.com'],
    fail_silently=False,
    )

    return True