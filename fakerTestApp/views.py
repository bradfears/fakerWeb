from django.shortcuts import render

from django.http import HttpResponse

from faker import Faker

import socket

fake = Faker()

hostName = socket.gethostname()

#content = "<p style='font-weight: bold; font-size: 30px;'>This page generates 25,000 fake email addresses. Its purpose is to simulate a load on a Kubernetes pod. Feel free to hit refresh, which should generate 25,000 new email addresses.</p><p style='font-size: 20px;'>Pod host name: <span style='font-weight: bold; color: green;'>" + hostName + "</span></p>"
#content = "<html><head><link rel='stylesheet' type='text/css' href='views.css'><script>$(window).load(function() { $('.loader').fadeOut('slow'); }); <script src='https://code.jquery.com/jquery-1.9.1.min.js'></script></script></head><body><div class='loader'></div><p style='font-weight: bold; font-size: 30px;'>This page generates 25,000 fake email addresses. Its purpose is to simulate a load on a Kubernetes pod. Feel free to hit refresh, which should generate 25,000 new email addresses.</p><p style='font-size: 20px;'>Pod host name: <span style='font-weight: bold; color: green;'>" + hostName + "</span></p></body></html>"
content = """

<!DOCTYPE html>
<html lang='en'>

<head>
    <style>
        #loader {
            border: 12px solid #f3f3f3;
            border-radius: 50%;
            border-top: 12px solid #444444;
            width: 70px;
            height: 70px;
            animation: spin 1s linear infinite;
        }

        .center {
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            margin: auto;
        }

        @keyframes spin {
            100% {
                transform: rotate(360deg);
            }
        }
    </style>
</head>

<body>
    <div id='loader' class='center'></div>

    <p style='font-weight: bold; font-size: 30px;'>This page generates 25,000 fake email addresses. Its purpose is to simulate a load on a Kubernetes pod. Feel free to hit refresh, which should generate 25,000 new email addresses.</p>
    <p style='font-size: 20px;'>Pod host name: <span style='font-weight: bold; color: green;'>""" + hostName + """</span></p>
        
    <script>
        document.onreadystatechange = function () {
            if (document.readyState !== 'complete') {
                document.querySelector(
                    'body').style.visibility = 'hidden';
                document.querySelector(
                    '#loader').style.visibility = 'visible';
            } else {
                document.querySelector(
                    '#loader').style.display = 'none';
                document.querySelector(
                    'body').style.visibility = 'visible';
            }
        };
    </script>
</body>

</html>
"""

def index(request):
    s = content
    for i in range(25000):    
        s = s + "Randomly Generated Email: " + fake.email() + "<br>"
    return HttpResponse(s)

