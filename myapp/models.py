from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(db_column='name', unique=True, max_length=100, blank=True, null=True)  
    description = models.TextField(db_column='description',  max_length=4000, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
        ordering = ['name']

    def __unicode__(self):
        return self.name

    def __str__(self): 
        return self.name