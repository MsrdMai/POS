from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
 

class Product(models.Model):

    # types = models.ForeignKey(Type, on_delete=models.PROTECT) 
    # #onetomany protectไม่สามารถลบได้เพราะอ้างอิงกับอีกตารางอยู่

    types = models.ForeignKey(Type, on_delete=models.PROTECT)
    name = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    
class Order(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()


class Order_Product(models.Model):
    order_id =  models.ForeignKey(Order, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
 
