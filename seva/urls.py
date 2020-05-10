from django.conf.urls import url
from .import views

urlpatterns =[
    url(r'^$', views.index, name='index'),
    url(r'^register$', views.register, name='register'),
    url(r'^login$', views.index, name='index'),
    url(r'^submit/$', views.registerSubmit, name='submit'),
    url(r'^form/$', views.loginSubmit, name='loginSubmit'),
    url(r'^dashboard/$', views.trial, name='dashboard'),
    url(r'^disease-form/$', views.diseaseSubmit, name='diseaseSubmit'),

    url(r'^doctor-form/(?P<id>\d+)/$', views.send, name='doctorSubmit'),
    # url(r'^doctor-form/$', views.doctorSubmit, name='doctorSubmit'),

]