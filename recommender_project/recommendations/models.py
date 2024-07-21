from django.db import models

class Tshirt(models.Model):
    product_id = models.CharField(max_length=50)
    height = models.FloatField()
    weight = models.FloatField()
    color_of_tshirt = models.CharField(max_length=50)
    size_of_tshirt = models.CharField(max_length=10)
    price = models.FloatField()

    def __str__(self):
        return f"{self.product_id} - {self.color_of_tshirt}"
