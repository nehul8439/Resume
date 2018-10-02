from django.shortcuts import render
from .forms import *
from .models import *
from django.http import HttpResponse
from django.core.mail import send_mail


# Create your views here.
def index(request):
	return render(request,'index.html')

	
def mail(request):
	subject="Greetings"
	msg		="This mail is send by django apps"
	to		="chauhanneha014@gmail.com"
	res		=send_mail(subject,msg,settings.EMAIL_HOST_USER, [to])
	if(res==1):
		msg="Mail sent successfully"
	else:
		msg="Mail coulsnot sent"
	return HttpResponse(msg)
	

def send(request):
	if request.method == "POST":  
		form = ResumeForm(request.POST)  
		to=request.POST['to']
		msg=request.POST['msg']
		subject=request.POST['subject']
		if form.is_valid():  
			res     = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])  
		if(res == 1):  
			msg = "Mail Sent Successfuly"  
		else:  
			msg = "Mail could not sent"   
	else:  
		form = ResumeForm()  
	return render(request,'index.html',{'form':form})     