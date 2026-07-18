from django.db import models
from accounts.models import *
from products.models import *
from orders.models import *



# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=(
        ('Pending','Pending'),
        ('Shipped','Shipped'),
        ('Delivered','Delivered'),
        ('Cancelled','Cancelled')
    )
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    total_price=models.DecimalField(default=0,max_digits=10,decimal_places=2)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Pending')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} -{self.user.username}"
    


class OrderItems(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.product.name


