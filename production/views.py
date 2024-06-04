from rest_framework import viewsets
from .models import ProductionRecord
from .serializers import ProductionRecordSerializer
from .repositories import ProductionRecordRepository

class ProductionRecordViewSet(viewsets.ModelViewSet):
    queryset = ProductionRecord.objects.all()
    serializer_class = ProductionRecordSerializer
    repository = ProductionRecordRepository()

    def get_queryset(self):
        return self.repository.get_all_records()

    def retrieve(self, request, *args, **kwargs):
        instance = self.repository.get_record_by_id(kwargs['pk'])
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        data = request.data
        record = self.repository.create_record(
            product_id=data['product_id'],
            production_date=data['production_date'],
            quantity=data['quantity'],
            shift=data['shift']
        )
        serializer = self.get_serializer(record)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        data = request.data
        instance = self.repository.update_record(
            kwargs['pk'],
            product_id=data.get('product_id'),
            production_date=data.get('production_date'),
            quantity=data.get('quantity'),
            shift=data.get('shift')
        )
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        self.repository.delete_record(kwargs['pk'])
        return Response(status=204)
