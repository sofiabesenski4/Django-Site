from django.db import models
from django.contrib.postgres.fields import JSONField
# Create your models here.

class Target(models.Model):
    #this is the URL primary key
    target_text = models.CharField(max_length=200)
    search_date= models.DateTimeField('date searched')
    body_text =models.CharField(max_length= 20000)
    def __str__(self):
        return self.target_text
class WordList(models.Model):
    target= models.ForeignKey(Target,on_delete=models.CASCADE, default=None)
    common_words= JSONField()
    def __str__(self):
        return str(self.common_words)