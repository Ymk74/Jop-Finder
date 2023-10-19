from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

# Create your models here.

JOP_TYPE = [
    ('Full_time','Full_time'),
    ('Part_time','Part_time'),
    ('Remote','Remote'),
    ('Freelance','Freelance'),
]


class Jop(models.Model):
    user = models.ForeignKey(User , related_name='jop_author' , on_delete=models.SET_NULL,null=True)
    jop_title = models.CharField(max_length=30)
    image = models.ImageField(upload_to='FindJops')
    company_name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    salary = models.IntegerField()
    created_at = models.DateField(default=timezone.now)
    jop_nature = models.CharField(max_length=10, choices=JOP_TYPE)

    def __str__(self):
        return self.jop_title
    