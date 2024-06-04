from django.db import models

class ProductionRecord(models.Model):
    product_id = models.CharField(max_length=50)
    production_date = models.DateField()
    quantity = models.IntegerField()
    shift = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_id} - {self.production_date}"