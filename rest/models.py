from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=20)
    body = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.created_at

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = "Posts"

class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=20)
    phone = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name
