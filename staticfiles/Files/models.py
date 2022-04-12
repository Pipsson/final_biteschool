
# Create your models here.
from django.db import models

# Create your models here.
class Advanced_math1(models.Model):
    adminupload = models.FileField(upload_to= 'media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
         
    
class Advanced_math2(models.Model):
    adminupload = models.FileField(upload_to='media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
    
class Physics1(models.Model):
    adminupload = models.FileField(upload_to='media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
    
class Physics2(models.Model):
    adminupload = models.FileField(upload_to='media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
         
    
class Chemistry1(models.Model):
    adminupload = models.FileField(upload_to='media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
    
class Chemistry2(models.Model):
    adminupload = models.FileField(upload_to='media')
    Year_Of_the_paper=models.IntegerField(default=2000)
    
         
 
class physics_form5(models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_book = models.CharField(max_length=20)
    
     

class Advance_math5(models.Model):
    adminupload = models.FileField(upload_to="media")
    Name_of_the_book = models.CharField(max_length=20)
    
    def  __str__(self):
        return self.Name_of_the_book    

class Chemistry_form5(models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_book = models.CharField(max_length=20)
    
    def  __str__(self):
        return self. Name_of_the_book    
class Advanced_math6(models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_book = models.CharField(max_length=20) 
    
    def  __str__(self):
        return self.Name_of_the_book    

class Chemistry_form6(models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_book = models.CharField(max_length=20)
    
    def  __str__(self):
        return self.Name_of_the_book      
    
class ChemistryPracticals (models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_practical = models.CharField(max_length=20)
    
    def  __str__(self):
        return self.Name_of_the_practical 
    
class physics_practicals (models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_practical = models.CharField(max_length=20)
    
    def  __str__(self):
        return self.Name_of_the_practical     

class physics_form6(models.Model):
    adminupload = models.FileField(upload_to='media')
    Name_of_the_book = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Name_of_the_book      
           
class Form(models.Model) :
    Name = models.CharField(max_length=25)
    Email = models.EmailField(max_length=100)
    Message = models.TextField(max_length=1000)
    
    def __str__(self):
        return self.Name
    