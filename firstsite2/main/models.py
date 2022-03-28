from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=50)
    content = models.TextField(null=True, blank=True)
    issued = models.DateTimeField(auto_now_add=True, db_index=True,
                                  null=True, verbose_name='Дата публиккации')
