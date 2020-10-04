from django.db import models 

from datetime import date
from mptt.fields import  TreeForeignKey
from django.urls import reverse
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.auth.models import User
















class Customer(models.Model):
    user=models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name





class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    slug=models.SlugField(null=False,unique=True)
    img = models.ImageField(upload_to='photos')


    def __str__(self):
        return self.name

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by=['name'] 
    


    def get_absolute_url(self):
    	return reverse('category_detail',kwargs={'slug':self.slug})
    


    def __str__(self):
    	full_path=[self.name] 
    	k=self.parent
    	while k is not None:
    	   	full_path.append(k.name)
    	   	k=k.parent
    	return '/'.join(full_path[::-1])
    



class alle(models.Model):
	objects=models.Manager()
	title=models.CharField(max_length=70)
	img = models.ImageField(upload_to='photos')
	description=models.TextField(verbose_name='Описание')
	fadescription=models.TextField(verbose_name='Описание')
	youtobevideo=models.CharField(max_length=170)
	Url = models.SlugField(max_length=130,null=False, unique=True )
	file = models.FileField(upload_to='files')
	mb=models.CharField(max_length=90)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
	class Meta:
            ordering=['-id']
	def get_absolute_url(self):
    		return reverse("blog:post_detail",args=[self.id,self.Url])
	
    


	
class Comment(models.Model):
    post = models.ForeignKey(alle, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.ForeignKey('Comment',null=True,on_delete=models.CASCADE, related_name='replies')
    content= models.TextField(max_length=160)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return '{}-{}'.format(self.post.title,str(self.user.username))