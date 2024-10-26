from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from teste.filters import ClientFilter, ProductFilter, EmployeeFilter, SaleFilter
from teste.models import Client, Product, Employee, Sale
from teste.serializers import ClientSerializer, ProductSerializer, EmployeeSerializer, SaleSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filterset_class = ClientFilter
    # permission_classes = {permissions.IsAuthenticated}


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    # permission_classes = {permissions.IsAuthenticated}

    @action(detail=False, methods=['GET'])
    def products_teste(self):
        products = self.queryset.get(id=1)
        pd_serializer = self.get_serializer(products)
        return Response(pd_serializer.data, status=200)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_class = EmployeeFilter
    # permission_classes = {permissions.IsAuthenticated}


class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    filterset_class = SaleFilter
    # permission_classes = {permissions.IsAuthenticated}
