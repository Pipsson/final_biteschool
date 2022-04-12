"""biteschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, re_path
from biteschool.settings import DEBUG , MEDIA_ROOT
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from Files import views






urlpatterns = [
    path('admin/', admin.site.urls),
    path('' ,views.homepage, name='home_return'),
    path('about/' ,views.aboutpage, name='about_return'),
    path('contact/' ,views.contactpage, name='contact_return'),
    path('paper/' ,views.paperpage, name='paper_return'),
    path('website/' ,views.webpage, name='web_return'),
    path('book/' ,views.bookpage, name='book_return'),
    path('book1/' ,views.book1page, name='book1_return'),
    path('Notes/' ,views.Notespage, name='Notes_return'),    
    path('practicals/' ,views.practicalspage, name='practicals_return'),     
    re_path(r'^download/(?P<path>.*)$',serve,{'document_root':MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns +=  static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns +=  static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
