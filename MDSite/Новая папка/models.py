from django.db import models 

from datetime import date

from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=20)

    


    def __str__(self):
        return self.name



    



class alle(models.Model):
	
	title=models.CharField(max_length=70)
	img = models.ImageField(upload_to='photos')
	description=models.TextField(verbose_name='Описание')
	fadescription=models.TextField(verbose_name='Описание')
	youtobevideo=models.CharField(max_length=170)
	Url = models.SlugField(max_length=130, unique=True )
	file = models.FileField(upload_to='files')
	mb=models.CharField(max_length=90)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	
	


	
