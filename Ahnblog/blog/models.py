from django.db import models
from django.conf import settings
# Create your models here.

class Post(models.Model):
	title=models.CharField(max_length=100, help_text='제목은 100글자')
	author=models.ForeignKey(settings.AUTH_USER_MODEL)
	content=models.TextField()
	photo=models.ImageField(blank=True, upload_to="uploads/%Y/%m/%d")
	create_at=models.DateTimeField(auto_now_add=True)
	update_at=models.DateTimeField(auto_now=True)


