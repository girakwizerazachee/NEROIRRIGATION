from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include, path
from . import views
from posts.views import *


urlpatterns = [

    path('', views.homepage, name="home"),
    path('summernote/', include('django_summernote.urls')),
    path('DetailService/<int:pk>', views.serviceDetail, name="ServiceDetail"),
    path('DetailGallery/<int:pk>', views.galleryDetail, name="GalleryDetail"),
    path('service/', views.post_list, name="posts"),
    path('register/', RegisterView.as_view(), name='register'),
    path('index/', views.homepage, name="questions"),
    path('adminhome/', views.adminHomePageView, name="adminHomePage"),
    path('post-list/', PostListView.as_view(), name="post-list"),
    path('login/', LoginView.as_view(), name="login"),
    path('contactus/', views.contactpage, name="contactus"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('aboutus/', views.aboutuspage, name="aboutus"),
    path('new-post/', NewPostView.as_view(), name ="new-post"),
    path('updateService/<int:pk>', edit.as_view(), name="edit"),
    path('updateGallery/<int:pk>', editGallery.as_view(), name="editGallery"),
    path('deleteService/<int:pk>', views.deleteService, name="deleteService"),
    path('deleteGallery/<int:pk>', views.deleteGallery, name="deleteGallery"),
    path('contact-list/', contactList.as_view(), name='contact-list'),
    path('new-Gallery/', NewGallery.as_view(), name ="new-gallery"),
    path('services/', views.servicepage, name="services"),
    path('portfolio/', views.portfoliopage, name="portfolio"),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('register/', RegisterView.as_view(), name='register'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)