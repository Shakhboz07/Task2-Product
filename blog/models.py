from django.db import models

class Products(models.Model):
    picture = models.ImageField(upload_to='product/')
    name = models.CharField(max_length=255)
    price = models.IntegerField()

    def __str__(self):
        return self.name

