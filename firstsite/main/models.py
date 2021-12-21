from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, primary_key=True)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    title = models.CharField('Name', max_length=50, blank=False)
    content = models.TextField(blank=False)
    issued = models.DateTimeField(blank=False)

    author = models.ForeignKey('Author', on_delete=models.CASCADE)

    def __str__(self):
        return self.titel

