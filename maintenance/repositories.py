from .models import MaintenanceRecord

class MaintenanceRecordRepository:
    def get_all_records(self):
        return MaintenanceRecord.objects.all()
    
    def get_record_by_id(self, record_id):
        return MaintenanceRecord.objects.get(id=record_id)
    
    def create_record(self, equipment_id, maintenance_date, technician, notes):
        record = MaintenanceRecord(
            equipment_id=equipment_id,
            maintenance_date=maintenance_date,
            technician=technician,
            notes=notes
        )
        record.save()
        return record
    
    def update_record(self, record_id, **kwargs):
        record = MaintenanceRecord.objects.get(id=record_id)
        for key, value in kwargs.items():
            setattr(record, key, value)
        record.save()
        return record
    
    def delete_record(self, record_id):
        record = MaintenanceRecord.objects.get(id=record_id)
        record.delete()
