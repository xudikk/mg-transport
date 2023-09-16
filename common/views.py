# from drf_yasg import openapi
# from drf_yasg.utils import swagger_auto_schema
# from rest_framework import generics
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.permissions import IsAuthenticated
# from rest_framework_api_key.permissions import HasAPIKey
#
# from apps.auto import models as auto_models
# from . import serializers, models
# from apps.auto.serializers import (
#     DepartmentListSerializer,
#     AutoColorListSerializer,
#     AutoModelListSerializer,
#     AutoMotoTransportListSerializer,
# )
#
#
# class RegionListAPIView(generics.ListAPIView):
#     queryset = models.Region.objects.all()
#     serializer_class = serializers.RegionSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class DistrictListAPIView(generics.ListAPIView):
#     queryset = models.District.objects.all()
#     serializer_class = serializers.DistrictSerializer
#     permission_classes = (IsAuthenticated,)
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = {
#         "region": ["exact", "in"]
#     }
#
#
# class DepartmentListAPIView(generics.ListAPIView):
#     queryset = auto_models.Department.objects.all()
#     serializer_class = DepartmentListSerializer
#     filter_backends = (DjangoFilterBackend,)
#     filterset_fields = {
#         "district": ["exact", "in"]
#     }
#
#
# class AutoColorListAPIView(generics.ListAPIView):
#     queryset = auto_models.AutoMotoTransportColor.objects.all()
#     serializer_class = AutoColorListSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class AutoModelListAPIView(generics.ListAPIView):
#     queryset = auto_models.AutoMotoTransportModel.objects.all()
#     serializer_class = AutoModelListSerializer
#     permission_classes = (IsAuthenticated,)
#
#
# class AutoMotoTransportListAPIView(generics.ListAPIView):
#     """
#     List of all AutoMotoTransport.
#     usage:
#         GET /api/v1/common/AutoMotoTransportList/
#
#         in headers:
#         Authorization: Api-Key <API_KEY>
#     """
#
#     queryset = auto_models.AutoMotoTransport.objects.all()
#     serializer_class = AutoMotoTransportListSerializer
#     permission_classes = (HasAPIKey,)
#
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         queryset = queryset.select_related(
#             "owner", "car_model", "color", "department"
#         )
#         return queryset
#
#     @swagger_auto_schema(
#         manual_parameters=[
#             openapi.Parameter(
#                 'Authorization',
#                 openapi.IN_HEADER,
#                 type=openapi.TYPE_STRING,
#                 description='Api-Key <your api-key>',
#                 pattern=r'Api-Key\s+[\w\d]+',
#                 required=True,
#             )
#         ]
#     )
#     def get(self, *args, **kwargs):
#         return super().get(*args, **kwargs)
