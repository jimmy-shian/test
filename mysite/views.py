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
		password = request.POST["inputPassword2"]

	if password == '1111' :

		return render(request,"manu.html",locals())
		
	else:

		return render(request,"index.html",locals()) 


def password(request):

	return render(request, "password.html", locals())

