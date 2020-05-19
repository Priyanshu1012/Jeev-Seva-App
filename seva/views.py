

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
import smtplib
from seva.mal import send_mail
from seva.models import Register, Animaldisease


def index(request):
    template = "login.html"
    context= {}
    return render(request,template,context)

def register(request):
    template = "register.html"
    context= {}
    return render(request,template,context)

def registerSubmit(request):
    if request.method == 'POST':
        name = request.POST['name']
        type = request.POST['type']
        mobileno = request.POST['mobileno']
        email = request.POST['email']
        password = request.POST['password']
        address = request.POST['address']
    data = Register(
        name = name,
        type = type,
        contact_no = mobileno,
        email = email,
        password = password,
        address = address
    )
    data.save()

    template="login.html"
    context={}
    return render(request,template,context)

def loginSubmit(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        try:
            valid = Register.objects.all().filter(name=name,password=password,type="User")
        except Exception as e:
            print(e)
        for i in valid:
            get_email = i.email
            get_pass = i.password
        if(valid):
            request.session['email'] = get_email
            request.session['password'] = get_pass
            return trial(request)
        else:
            return HttpResponse('FIRST YOU HAVE TO REGISTER')

def trial(request):
    template = "dashboard.html"
    doctor_data = Register.objects.all()
    context= {'doctor_data': doctor_data}
    return render(request,template,context)

def diseaseSubmit(request):
    if request.method == 'POST':
        type = request.POST['type']
        disease = request.POST['disease']
        priority = request.POST['priority']
        description = request.POST['description']
    data = Animaldisease(
        type=type,
        disease=disease,
        priority=priority,
        description=description
    )
    data.save()

    template = "doctor.html"
    doctor_data = Register.objects.all().filter(type = "Doctor")
    context = {'doctor_data': doctor_data}
    return render(request,template,context)




def send(request,id):
    try:
        valid = Register.objects.all().filter(id=id)
        animal_info = Animaldisease.objects.last()
        animal_type = animal_info.type
        animal_disease = animal_info.disease
        animal_priority = animal_info.priority
        describe = animal_info.description
    except Exception as e:
        print(e)

    for i in valid:
        send_email_data = i.email

    senders_address = "priyanshukhandelwal101@gmail.com"
    receivers_address = send_email_data
    SUBJECT = "JEEV SEVA: DISEASE DETAILS"

    text = 'Animal Type      = ' + animal_type + '\n' + 'Animal Disease    = ' + animal_disease + '\n' + \
           'Availability Status = ' + animal_priority + '\n' + 'Description        = ' + describe
    message = 'Subject: {}\n\n{}'.format(SUBJECT, text)
    mail = smtplib.SMTP("smtp.gmail.com", 587)
    mail.ehlo()
    mail.starttls()

    mail.login(senders_address, "#########")
    mail.sendmail(senders_address, receivers_address, message)
    print("Successfully sent email to {receivers_address}")
    mail.close()

    return HttpResponse("<h1>MAIL SENT</h1>")

    # try:
    #     valid = Register.objects.all().filter(id=id)
    # except Exception as e:
    #     print(e)
    # for i in valid:
    #     send_email_data = i.email
    #
    # send_mail('Django mail',
    #           'hello',
    #           'priyanshukhandelwal101@gmail.com',
    #           [send_email_data],
    #           fail_silently=False)
    #
    # return HttpResponse('mail sent')




