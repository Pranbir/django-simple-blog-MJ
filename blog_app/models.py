from django.db import models
from tinymce import models as tinymce_models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = tinymce_models.HTMLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title