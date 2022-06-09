from django.shortcuts import render
from django.http import HttpResponse
import random, datetime
from mysite import models
from django.template import RequestContext
from http import HTTPStatus

#from flask import Flask, redirect, url_for, render_template,request

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
 
def index(request):
	posts = models.Post.objects.all()	
	return render(request, "index.html", locals())

def manu(request):

	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        #form = NameForm(request.POST)
        # check whether it's valid:
        #if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
		password = request.POST["inputPassword2"]
        #sss = request.POST.get('inputPassword2')
	if password == '1111' :
		return render(request,"manu.html",locals())

	# if a GET (or any other method) we'll create a blank form
	else:
		context = {"error": "Error"}
		#form = NameForm()
		# return render(request,"lotto.html",locals())
		return render(request,"index.html",locals()) 


def password(request):

	return render(request, "password.html", locals())

