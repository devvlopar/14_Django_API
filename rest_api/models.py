from django.db import models

# Create your models here.
class Cities(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    passwd = models.CharField(max_length=30)
    address = models.TextField()
    mobile = models.CharField(max_length=15)
    city = models.ForeignKey(Cities, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.first_name