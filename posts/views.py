from django.shortcuts import render
from .forms import NewPostForm,NewGelleryForm
from django.views.decorators.cache import cache_control
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Service,Question,Gallery
from django.contrib.auth.views import LogoutView
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DetailView
from .forms import LoginForm,UserRegistration
from django.contrib.auth.views import LoginView
from unicodedata import category
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
import json, datetime
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import Savecontact
from . import forms
from django.urls import reverse_lazy





# Create your views here.
def post_list(request):
    posts = Service.objects.all()
    return render(request, 'service.html', {'posts':posts})


def contactpage(request):
    return render(request, 'contact.html')


def homepage(request):
    questions = Question.objects.all()[:3]
    gallery = Gallery.objects.all()[:5]
    context = {}
    context['gallery'] = gallery
    context['questions'] = questions
    return render(request, 'index.html',context)
    

def servicepage(request):
    posts = Service.objects.all()
    return render(request, 'services.html', {'posts':posts})


def aboutuspage(request):
    return render(request, 'aboutus.html')

def portfoliopage(request):
    gallery = Gallery.objects.all()
    return render(request, 'portfolio.html', {'gallery':gallery})

def adminpage(request):
    return render(request, 'admin/login.html')


def savecontact(request):
    if request.method == 'POST':
        form = Savecontact(request.POST)
        if form.is_valid():
          form.save()
          return redirect('contactus')
        
        
        else:
         form = Savecontact()
       
    return  redirect('contactus')


# register view
class RegisterView(CreateView):
    form_class = UserRegistration
    success_url = reverse_lazy('login')
    template_name = 'admin/signup.html'

class contactList(LoginRequiredMixin, ListView):
    template_name = 'admin/contact-list.html'
    model = Question
    context_object_name = 'contact'

# admin side views
@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminHomePageView(request):
    posts = Service.objects.all()
    return render(request, 'admin/home.html', {'posts':posts})
    

#delete Service
def deleteService(request,pk):
    Servicedelete = Service.objects.get(id=pk)
    Servicedelete.delete()
    return redirect('adminHomePage')

#delete Gallery
def deleteGallery(request,pk):
    Galleryedelete = Gallery.objects.get(id=pk)
    Galleryedelete.delete()
    return redirect('post-list')
# lNew posts

class NewPostView(LoginRequiredMixin, CreateView):
    form_class = NewPostForm
    success_url = ('../adminhome')
    template_name = 'admin/new-post.html'

# New Gallery
class NewGallery(CreateView):
    form_class = NewGelleryForm
    success_url = ('../post-list')
    template_name = 'admin/new-gallery.html'

#update gallery
class edit(UpdateView):
    model = Service  # required
    template_name = 'admin/editService.html'
    form_class = NewPostForm
    success_url = reverse_lazy('adminHomePage')

    def get_queryset(self):
        """
        Optional condition to restrict what users can see
        """
        queryset = super().get_queryset()
        return queryset.filter(id__lt=20)

    def get_success_url(self):
        return reverse_lazy(
            'adminHomePage',
            
        )
#update gallery
class editGallery(UpdateView):
    model = Gallery  # required
    template_name = 'admin/editGallery.html'
    form_class = NewGelleryForm
    success_url = reverse_lazy('post-list')

    def get_queryset(self):
        """
        Optional condition to restrict what users can see
        """
        queryset = super().get_queryset()
        return queryset.filter(id__lt=20)

    def get_success_url(self):
        return reverse_lazy(
            'post-list',
            
        )

# post list view
class PostListView(LoginRequiredMixin, ListView):
    template_name = 'admin/post-list.html'
    model = Gallery
  
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        post_num= Gallery.objects.all().count()
        all_post = Gallery.objects.all()

        context['post_num'] = post_num
        context['all_post'] = all_post
        return context

#Service detail view
def serviceDetail(request, pk):
    
    servicepost = Service.objects.get(id=pk)
    
    return render(request, 'admin/servicedetail.html', context={'servicepost': servicepost})

#Gallery detail view
def galleryDetail(request, pk):
    
    Gallerypost = Gallery.objects.get(id=pk)
    
    return render(request, 'admin/gallerydetail.html', context={'Gallerypost': Gallerypost})

# login view
class LoginView(LoginView):
    form_class = LoginForm
    template_name = 'admin/login.html'
    success_url = 'adminHomePage'


class LogoutView(LogoutView):
    next_page = 'login'