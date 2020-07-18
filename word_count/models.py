from django.db import models

# Create your models here.

class Target(models.Model):
    #this is the URL primary key
    target_text = models.CharField(max_length=200)
    search_date= models.DateTimeField('date searched')
    def __str__(self):
        return self.target_text

class Body(models.Model):

    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    body_text =models.CharField(max_length= 5000)
    def __str__(self):
        return self.body_text