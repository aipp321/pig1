from django.db import models

# Create your models here.
class Order(models.Model):
    agent = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    avg_weight = models.CharField(max_length=50)
    per_weight_price = models.CharField(max_length=50)
    c_time = models.DateTimeField('日期', default=date.today)


    def __str__(self):
        return self.agent + self.c_time