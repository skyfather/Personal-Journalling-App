from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Journal(models.Model):
    title = models.CharField(max_length=300)
    owner = models.ForeignKey(User, related_name="journals", on_delete=models.CASCADE)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created = models.DateField(auto_now=False, auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title
    
