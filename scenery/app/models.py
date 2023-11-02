
        
from django.db import models

class Pic(models.Model):
    pic_label = models.IntegerField(default=0)
    pic_name =  models.CharField(max_length=100, default='')
    pic_intro =  models.CharField(max_length=100, default='')
    pic_link =  models.CharField(max_length=100, default='')
    

    def __str__(self):
        return self.pic_name