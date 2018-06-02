# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
# from .forms import ProductForm

def index(request):
	context = {}
	return render(request, 'homework/index.html', context)

# @login_required
# def product(request):
# 	context = {}
# 	if request.method == "POST":
# 		form = ProductForm(request.POST, user_id=request.user.id)
# 		if form.is_valid():
# 			db_name = form.cleaned_data['database_name']
# 			product_name = form.cleaned_data['product_name']
# 			product = Product(name=product_name, user_id=request.user.id, db_name=db_name)
# 			product.save(using=db_name)
# 			context["message"] = "Product added successfully."
# 		else:
# 			return render(request, 'db_mgmt/product.html', context)
			
# 	context["form"] = ProductForm(user_id=request.user.id)
# 	return render(request, 'db_mgmt/product.html', context)
