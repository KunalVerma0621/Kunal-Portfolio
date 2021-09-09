from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from pofo import models


# Create your views here.
def landing(request):
    return render(request,'pofo/index.html')

def information(request):
    if request.method=='POST':
        sms= models.Message()
        sms.name=request.POST['name']
        sms.email=request.POST['email']
        sms.phone=request.POST['number']
        sms.inbox=request.POST['message']
        if len(sms.name)<2 or len(sms.email)<3 or len(sms.phone)<10 or len(sms.inbox)<4:
          msg="Oops! Something is wrong in your detail."
          sub=False
        else:
           sms.save()
           sub=True
           msg="Congratulations! You response has been received.You are a new member of our society."
    #msg=msg+'<br><a href="http://localhost:8000/pofo/landing/">landing</a>'
    messages={'msg':msg,'sub':sub}
    return render(request,'pofo/response.html',messages)
