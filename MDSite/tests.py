from django.test import TestCase

filtere=stat.filter(type1='soft')
# Create your views here.
# Create your tests here.
class FeildView(ListView):
	def get(self,request,slug):
		statie=alle.objects.get(type1=slug)
		filtere=stat.filter(type1='soft')
		return render(request,"MDSite/main.html",{"statie":statie})
class Category(models.Model):
    name = models.CharField(max_length=20)

    


    def __str__(self):
        return self.name

category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)




{% endrecursetree %}









alles=None
		categories=Category.get_all_categories()

	   		

	   		categoryID=request.GET.get('category')
	   	if categoryID:
	   		alles=alle.get_all_products_by_categoryid(categoryID)

	   	else:
	   		alles=alle.objects.all();