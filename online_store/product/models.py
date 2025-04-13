from django.db import models

# Create your models here.


class Product(models.Model):
    title  = models.CharField(max_length=2048)
    content  = models.TextField()
    types = models.CharField(max_length=2048, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    quantity = models.IntegerField(default=0)
    product_image = models.ImageField(upload_to="images/")
    
    def __str__(self):
        return f"{self.types} is {self.title}"

