from django.db import models

# Create your models here.


class SupportRequests(models.Model):
    user_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    DOB = models.DateField()
    email = models.EmailField()
    ip = models.CharField(max_length=30)
    description = models.TextField()

    class Meta:
        db_table = 'support_requests'

    def __str__(self):
        return  self.user_name