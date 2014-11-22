# coding:utf-8
from django.db import models

# class Person(models.Model):
    # name = models.CharField(max_length=30)
    # age = models.IntegerField()

    # def __unicode__(self):
	    # return self.name
        
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(u'年龄')
    
    def my_property(self):
        return self.first_name + ' ' + self.last_name
    my_property.short_description = "Full name of the person"
    
    full_name = property(my_property)