from django.db import models


class MaintenanceRecord(models.Model):
    equipment_id = models.CharField(max_length=50)
    maintenance_date = models.DateField()
    technician = models.CharField(max_length=100)
    notes = models.TextField()

    def __str__(self):
        return f"{self.equipment_id} - {self.maintenance_date}"

