

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from seva.mal import send_mail
from seva.models import *
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
# from googlemaps import * 
def index(request):
    template = "index.html"
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

    template="index.html"
    context={}
    return render(request,template,context)

def loginSubmit(request):
    if request.method == 'POST':
        email = request.POST['email']
        print(email)
        password = request.POST['password']
        try:
            valid = Register.objects.all().filter(email=email,password=password,type="User")
        except Exception as e:
            print(e)
        for i in valid:
            get_email = i.email
            get_pass = i.password
        print(valid)
        if(valid):
            request.session['email'] = get_email
            request.session['password'] = get_pass
            return trial(request)
        else:            
            return render(request,"index.html",{'error':1})

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
        print(request.FILES['image'])
        image = request.FILES['image']
        description = request.POST['description']
    data = Animaldisease(
        type=type,
        disease=disease,
        priority=priority,
        image=image,
        description=description
    )
    data.save()

    mapbox_access_token = 'pk.my_mapbox_access_token'
    template = "default.html"
    doctor_data = Register.objects.all().filter(type = "Doctor")
    print(doctor_data)
    context = {'doctor_data': list(doctor_data),'mapbox_access_token': mapbox_access_token}
    return render(request,template, context)




def send(request,id):
    try:
        valid = Register.objects.all().filter(id=id)
        animal_info = Animaldisease.objects.last()
        animal_type = animal_info.type
        animal_disease = animal_info.disease
        animal_priority = animal_info.priority
        animal_image = animal_info.image.name
        describe = animal_info.description
    except Exception as e:
        print(e)

    for i in valid:
        send_email_data = i.email
    
    receivers_address = send_email_data
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(BASE_DIR, 'static\\images\\') + animal_image
    img_data = open(path, 'rb').read()
    msg = MIMEMultipart()
    msg['Subject'] = 'JEEV SEVA: DISEASE DETAILS'
    msg['From'] = 'priyanshukhandelwal101@gmail.com'
    msg['To'] = receivers_address

    text_msg = 'Animal Type = ' + animal_type + '\n' + 'Animal Disease = ' + animal_disease + '\n' + \
           'Availability Status = ' + animal_priority + '\n' + 'Description = ' + describe

    text = MIMEText(text_msg)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename(path))
    msg.attach(image)

    s = smtplib.SMTP('smtp.gmail.com', 587  )
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login('priyanshukhandelwal101@gmail.com', 'Khandelwal@123')
    s.sendmail(msg['From'], msg['To'], msg.as_string())
    s.quit()

    mapbox_access_token = 'pk.my_mapbox_access_token'
    template = "default.html"
    doctor_data = Register.objects.all().filter(type = "Doctor")
    print(doctor_data)
    context = {'doctor_data': list(doctor_data),'mapbox_access_token': mapbox_access_token}
    return render(request,"default.html",{'error':1})


def default_map(request):
    # TODO: move this token to Django settings from an environment variable
    # found in the Mapbox account settings and getting started instructions
    # see https://www.mapbox.com/account/ under the "Access tokens" section
    mapbox_access_token = 'pk.my_mapbox_access_token'
    template = "default.html"
    doctor_data = Register.objects.all().filter(type = "Doctor")
    print(doctor_data)
    context = {'doctor_data': list(doctor_data),'mapbox_access_token': mapbox_access_token}
    return render(request,template, context)





