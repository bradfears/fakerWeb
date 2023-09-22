from django.shortcuts import render

from django.http import HttpResponse

from faker import Faker

import socket

fake = Faker()

hostName = socket.gethostname()

def index(request):
    s = "<p style='font-weight: bold; font-size: 30px;'>This page generates 25,000 fake email addresses. Its purpose is to simulate a load on a Kubernetes pod. Feel free to hit refresh, which should generate 25,000 new email addresses.</p><p style='font-size: 20px;'>Pod host name: <span style='font-weight: bold; color: green;'>" + hostName + "</span></p>"
    for i in range(25000):    
        s = s + "Randomly Generated Email: " + fake.email() + "<br>"
    return HttpResponse(s)

