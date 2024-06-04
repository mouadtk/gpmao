from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MaintenanceRecordSerializer
from .models import MaintenanceRecord
from .repositories import MaintenanceRecordRepository

class MaintenanceRecordViewSet(viewsets.ModelViewSet):
    queryset = MaintenanceRecord.objects.all()
    serializer_class = MaintenanceRecordSerializer
    repository = MaintenanceRecordRepository()

    def get_queryset(self):
        return self.repository.get_all_records()

    def retrieve(self, request, *args, **kwargs):
        instance = self.repository.get_record_by_id(kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        record = self.repository.create_record(
            equipment_id=data['equipment_id'],
            maintenance_date=data['maintenance_date'],
            technician=data['technician'],
            notes=data['notes']
        )
        serializer = self.get_serializer(record)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.repository.update_record(
            kwargs['pk'],
            equipment_id=data.get('equipment_id'),
            maintenance_date=data.get('maintenance_date'),
            technician=data.get('technician'),
            notes=data.get('notes')
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.repository.delete_record(kwargs['pk'])
        return Response(status=204)
