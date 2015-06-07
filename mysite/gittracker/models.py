from django.db import models

# Create your models here.


class FileName(models.Model):
        
        name = models.CharField(max_length=200)
	checked_out = models.BooleanField(default=False)
	owner = models.CharField(max_length=200)
	time_inserted = models.DateTimeField()	

        def __str__(self):
                return ('%s\n')%self.name



