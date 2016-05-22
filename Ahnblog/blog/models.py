from django.db import models

# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=100, help_text='제목은 100글자')
	content=models.TextField()
	photo=models.ImageField(blank=True)
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)
