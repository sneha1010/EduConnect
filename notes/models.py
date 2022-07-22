from django.contrib.auth.models import User
from django.db import models


status_choice=(
    ('pending','pending'),
    ('accept','accept'),
    ('reject','reject')
)
class Notes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    uploadingdate = models.CharField(max_length=30)
    branch = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    notesfile = models.FileField(null=True)
    filetype = models.CharField(max_length=30)
    description = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=15,default='pending',choices=status_choice)

    # def __str__(self):
    #     return str(self.name)
