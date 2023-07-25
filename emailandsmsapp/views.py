from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.conf import settings
import requests
from django.http import HttpResponse
# Create your views here.
otp=str(random.randint(10000000,99999999))
def input(request):
    return render(request,'input.html')
def reg(request):
    fn=request.POST['t1']
    ln=request.POST['t2']
    un=request.POST['t3']
    pw=request.POST['t4']
    cpwd=request.POST['t5']
    mailid=request.POST['t6']
    mobno=request.POST['t7']
    send_mail('reg otp',otp,settings.EMAIL_HOST_USER,[mailid],fail_silently=True)
    resp = requests.post('https://textbelt.com/text', {
        'phone': str(mobno),
        'message': otp,
        'key': '21b856bbb43292ad45fd6c80c33720af114b8c80ZB0rNp3lRJO6EaAvaeKJWZ8m6', })
    print(otp)
    return HttpResponse("otp send to email and mobile number")
