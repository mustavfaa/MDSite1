from django.shortcuts import render,redirect

from django.views.generic.base import View

from django.contrib.auth.decorators import login_required
from .models import alle,Category,Customer,Comment
from django.views.generic.base import View
from django.urls import reverse
from django.shortcuts import render
import datetime
from django.conf import settings
from django.db.models import Q
from django.http import JsonResponse, HttpResponse,HttpResponseRedirect
from django.shortcuts import redirect,render,get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth import authenticate,login,logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views import View
from django.core.paginator import Paginator
from django.contrib import messages
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect, HttpResponsePermanentRedirect,JsonResponse
from django.template.loader import render_to_string


class MDSiteView(ListView):
	def get(self,request):
		
		search_query=request.GET.get('search','')

		if search_query:
			stat=alle.objects.filter(title__icontains=search_query)

		else:
		    stat=alle.objects.all()
		paginator = Paginator(stat, 3)
		page_number=request.GET.get('page',1)
		page=paginator.get_page(page_number)

		
		
		if page.has_next():
			next_url=f'?page={page.next_page_number()}'
		else:
			next_url=''

		if page.has_previous():
			prev_url=f'?page={page.previous_page_number()}'
		else:
			prev_url=''
		
		category=Category.objects.all()
		customers=Customer.objects.all()


		return render(request,"MDSite/index.html",{"page":page,
			'next_page_url':next_url,'prev_page_url':prev_url,'category':category,'customers':customers})
			

		
	      


def post_detail(request,slug,):
	try:
		post=alle.objects.get(Url=slug)
	except:
		raise Http404("Post Does Not Exist")	

	

		

	random = alle.objects.order_by('?')[:4]	
	category=Category.objects.all()
	comments=Comment.objects.filter(post=post,reply=None).order_by('-id')

	if request.method=='POST':
		comment_form=CommentForm(request.POST or None)
		if comment_form.is_valid():
			content=request.POST.get('content')
			reply_id=request.POST.get('comment_id')
			comment_qs=None
			if reply_id:
				comment_qs=Comment.objects.get(id=reply_id)

			comment=Comment.objects.create(post=post,user=request.user,content=content,reply=comment_qs)
			comment.save()
			
			
	else:
		comment_form=CommentForm


	context={'comment_form':comment_form,'comments':comments, 'category':category,"post":post}
	context1={'comment_form':comment_form,'comments':comments, 'category':category,"post":post,'random':random}


	if request.is_ajax():
		html=render_to_string('include/comment.html' ,context , request=request)
		return JsonResponse( { 'form' : html} )

	
	return render(request,"MDSite/base.html", context1)







		

def category_alle(request,id,slug):
		
		alles=alle.objects.filter(category_id=id)
		
		category=Category.objects.all()
		paginator = Paginator(alles, 3)
		page_number=request.GET.get('page',1)
		page=paginator.get_page(page_number)

		
			
		
		
		if page.has_next():
			next_url=f'?page={page.next_page_number()}'
		else:
			next_url=''

		if page.has_previous():
			prev_url=f'?page={page.previous_page_number()}'
		else:
			prev_url=''
		return  render(request,"MDSite/main.html",{"page":page,
			'next_page_url':next_url,'prev_page_url':prev_url,'category':category,"alles":alles})

		
def loginPage(request):

		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')
			user = authenticate(request, username=username, password=password)
			

			if user is not None:
				login(request, user)
				return redirect('index')
			else:
				messages.info(request, 'Username OR password is incorrect')

		contex={}
		return  render(request,"MDSite/login.html",contex)



def logoutUser(request):
	logout(request)
	return redirect('login')


def registerPage(request):
		form=CreateUserForm()

		if request.method=='POST':
			form=CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				
				user.groups.add(group)
				#Added username after video because of error returning customer name if not added
				Customer.objects.create(
					user=user,
					name=user.username,
					)

				messages.success(request, 'Account was created for ' + user)
				messages.success(request,'')
				return redirect('login')





		contex={'form':form}
		return  render(request,"MDSite/register.html",contex)

def userPage(request):
		orders=request.user.customer.order_set.all()
		return  render(request,"MDSite/user.html",{'orders':orders})

def accountSettings(request):
	customer = request.user.customer
	form = CustomerForm(instance=customer)

	if request.method == 'POST':
		form = CustomerForm(request.POST, request.FILES,instance=customer)
		if form.is_valid():
			form.save()


	context = {'form':form}
	return render(request, 'MDSite/account_settings.html', context)
