from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE) 
    # on_delete=models.CASCADE : When the referenced object is deleted, also delete the objects 
    # that have references to it (When you remove a blog post for instance, 
    # you might want to delete comments as well).

    def __str__(self):
        return self.title
    