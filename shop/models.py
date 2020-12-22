from django.db import models
from datetime import datetime

class Product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(default="dfg", max_length=50)
    desc=models.CharField(default="stest", max_length=300)
    pub_date=models.DateField()