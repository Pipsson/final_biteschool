from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from Files.models import Advanced_math1,Advanced_math2,Physics1, Physics2,Chemistry1,Chemistry2,physics_form5,Advance_math5,Chemistry_form5,Advanced_math6,Chemistry_form6, physics_form6,Form,physics_practicals,ChemistryPracticals
import os
from urllib import response


# Create your views here.
#def download(request,path):
#   file_path = os.path.join(settings.MEDIA_ROOT,path)
    
 #   if os.path.exists(file_path):
  #      with open(file_path, 'rb') as fh:
   #         response = HttpResponse(fh.read(), content_type = "application/adminupload")
    #        response ['content - Disposition'] = 'inline; filename =' + os.path.basename(file_path)
     #       return response
        
   # raise Http404





def homepage(request):
     if request.method =="POST":
         
            form = Form()
            name = request.POST.get('name')
            email= request.POST.get('email')
            message= request.POST.get('message')
            form.Name = name
            form.Email = email
            form.Message = message
            form.save()
       
            return HttpResponse('<h1>Your form has been submitted successfully </h1>')
     return render(request ,'Files/home.html')
def webpage(request):
    
    return render(request ,'Files/website.html')

def contactpage(request):
    if request.method =="POST":
        form = Form()
        name = request.POST.get('name')
        email= request.POST.get('email')
        message= request.POST.get('message')
        form.Name = name
        form.Email = email
        form.Message = message
        form.save()
       
        return HttpResponse('<h1>Your form has been submitted successfully </h1>')
    return render(request ,'Files/contact.html')

def aboutpage(request):
    return render(request ,'Files/about.html')


def paperpage(request):
    Context = { "File":Advanced_math1.objects.all(),
                "File2":Advanced_math2.objects.all(),
                "File3":Physics1.objects.all(),
                "File4":Physics2.objects.all(),
                "File5":Chemistry1.objects.all(),
                "File6":Chemistry2.objects.all(),
            
               }   
    return render(request ,'Files/paper.html',Context)
   
   

def bookpage(request):
    context1 = { "File1":Chemistry_form5.objects.all(),
                 "File2":physics_form5.objects.all(),
                 "File3":Advance_math5.objects.all(),
        
    }
    return render(request ,'Files/book.html', context1)

def book1page(request):
    context2 = { "File1":Chemistry_form6.objects.all(),
                 "File2":physics_form6.objects.all(),
                 "File3":Advanced_math6.objects.all(),
        
              }
    return render(request ,'Files/book1.html', context2)

def practicalspage(request):
    context3 = { "File1":ChemistryPracticals.objects.all(),
                 "File2":physics_practicals.objects.all(),
                 
        
              }
    return render(request ,'Files/practicals.html', context3)

def Notespage(request):
    return render(request ,'Files/Notes.html')

