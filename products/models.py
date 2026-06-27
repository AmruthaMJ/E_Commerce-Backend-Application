from django.db import models

# Create your models here.
class Category(models.Model):
    category=models.CharField(max_length=100,unique=True)
    description=models.TextField(blank=True)

    def __str__(self):
        return self.category

class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='products'),
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    stock=models.PositiveIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
