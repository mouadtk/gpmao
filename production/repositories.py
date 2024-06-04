from .models import ProductionRecord

class ProductionRecordRepository:
    def get_all_records(self):
        return ProductionRecord.objects.all()
    
    def get_record_by_id(self, record_id):
        return ProductionRecord.objects.get(id=record_id)
    
    def create_record(self, product_id, production_date, quantity, shift):
        record = ProductionRecord(
            product_id=product_id,
            production_date=production_date,
            quantity=quantity,
            shift=shift
        )
        record.save()
        return record
    
    def update_record(self, record_id, **kwargs):
        record = ProductionRecord.objects.get(id=record_id)
        for key, value in kwargs.items():
            setattr(record, key, value)
        record.save()
        return record
    
    def delete_record(self, record_id):
        record = ProductionRecord.objects.get(id=record_id)
        record.delete()
