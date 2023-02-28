from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)


# class Notes(models.Model):
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     reminder = models.DateTimeField(auto_now=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='notes', null)

