from django.db import models

# Create your models here.
class Blogs(models.Model):
	title = models.CharField(max_length=100)
	text = models.CharField(max_length=750)
	link = models.CharField(max_length=100, blank = True)

	def __str__(self):
		return self.title