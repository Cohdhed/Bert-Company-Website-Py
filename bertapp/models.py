from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    email = models.EmailField()
    message = models.TextField()
    #sent = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
