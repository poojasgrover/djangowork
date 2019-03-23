# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.template import Template, Context
from django.template.loader import get_template
from django.template import loader


def index(request):
	return HttpResponse("Hello, world. You're at the HelloWorld index.")



def my_index(request):
	template=loader.get_template('index.html')
	google_analytics=1
	context={'google_analytics':google_analytics,}
	return HttpResponse(template.render(context,request))

