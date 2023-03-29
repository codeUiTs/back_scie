import datetime
import json
import os
import pandas as pd
from django.utils.timezone import now
from django.http import HttpResponse
from pathlib import Path
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.parsers import JSONParser, MultiPartParser
from apps.base.utils import CustomDjangoModelPermissions, html_to_pdf
from apps.facturaProveedor.api.serializers import FpSerializer, ListFpSerializer, ProveedorSerializer, ReportFpSerializer
from apps.facturaProveedor.models import FacturaProveedor, Proveedor

BASE_DIR = Path(__file__).resolve().parent.parent

class FpViewSet(viewsets.GenericViewSet):
    model = FacturaProveedor
    serializer_class = FpSerializer
    list_serializer_class = ListFpSerializer
    list_Proveedors_class = ProveedorSerializer
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
            record_serializer = FpSerializer(record)
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

    @action(methods=['GET'], detail=False, url_path="Proveedors", url_name="Proveedors")
    def ListProveedors(self, request):
        Proveedors = ProveedorSerializer(Proveedor.objects.all(), many=True)
        
        return Response(Proveedors.data, status=status.HTTP_200_OK)
    
    @action(methods=['GET'], detail=False, url_path="generateReport", url_name="generateReport")
    def generateReport(self, request):
        Activo = ReportFpSerializer(self.get_queryset(), many=True)
        dir = os.path.abspath(os.path.dirname(__name__))
        fecha_actual = datetime.datetime.now().date()
        demo_df = pd.DataFrame(Activo.data)
        demo_df = demo_df.fillna(0)
        demo_df.rename(columns={'id':'ID','producto':'Producto', 'Proveedor':'Proveedor', 'fecha_factura':'Fecha', 'importe':'Importe'}, inplace=True)
        html_string = '''
        <html>
        <head><title>{title}</title></head>
        <link rel="stylesheet" type="text/css" href="{styles}"/>
        <body>
        <header>
            <nav>
            <img src="{img}" alt="icon" style="width:40px;float:right;">
            <br />
            <h1> Reporte de {title} </h1>
            <h1> Fecha: {time} </h1>
            </nav>
        </header>
            {table}
        </body>
        </html>.
        '''

        with open("files/docs/myhtml.html", 'w') as f:
            f.write(html_string.format(table=demo_df.to_html(classes='styled-table', index=False), styles=f"{dir}/files/css/pdfStyles.css", img=f"{dir}/files/assets/icon.png", title="Facturas Proveedor", time=fecha_actual))
        pdf = html_to_pdf('files/docs/myhtml.html')
         
         # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')
        
        
