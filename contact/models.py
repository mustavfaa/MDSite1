from django.db import models

class Contact(models.Model):
	first_name=email=models.CharField(max_length=80)
	email=models.CharField(max_length=80)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.email
