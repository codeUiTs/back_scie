import json
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.base.utils import CustomDjangoModelPermissions
from apps.facturaCliente.api.serializers import FcSerializer, ListFcSerializer, ClienteSerializer
from apps.facturaCliente.models import FacturaCliente, Cliente


class FcViewSet(viewsets.GenericViewSet):
    model = FacturaCliente
    serializer_class = FcSerializer
    list_serializer_class = ListFcSerializer
    list_clientes_class = ClienteSerializer
    parser_classes = (JSONParser, MultiPartParser)
    queryset = None
    permission_classes = [CustomDjangoModelPermissions]
    
    def get_object(self, pk):
        obj = get_object_or_404(self.model, pk=pk)
        self.check_object_permissions(self.model, obj)
        return obj

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    def list(self, request):
        users = self.get_queryset()
        Activo = self.list_serializer_class(users, many=True)
        return Response(Activo.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registro creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response({'message': '', 'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        record = self.get_queryset(pk)
        if record:
            record_serializer = FcSerializer(record)
            return Response(record_serializer.data, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        if self.get_queryset(pk):
            record_serializer = self.serializer_class(
                self.get_queryset(pk), data=request.data)
            if record_serializer.is_valid():
                record_serializer.save()
                return Response({'message': 'record actualizado correctamente!'}, status=status.HTTP_200_OK)
            return Response({'message': '', 'error': record_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        record = self.get_queryset().filter(id=pk).first()
        if record:
            record.delete()
            return Response({'message': 'Record eliminado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PATCH'])
    def robject(self, request, pk=None):
        record = self.get_queryset().filter(id=pk).first()
        if record:
            record.r_object = json.loads(request.data['r_object'])
            record.save()
            return Response({'message': 'r_object actualizado correctamente!'}, status=status.HTTP_200_OK)
        return Response({'error': 'No existe un record con estos datos!'}, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['GET'], detail=False, url_path="clientes", url_name="clientes")
    def ListClientes(self, request):
        Clientes = ClienteSerializer(Cliente.objects.all(), many=True)
        
        return Response(Clientes.data, status=status.HTTP_200_OK)

