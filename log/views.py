# from django.http import HttpResponse, JsonResponse

from .models import Push, Sms, User, File, Spnavigator, Lk
from rest_framework.generics import ListCreateAPIView, ListAPIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework import filters, status
from rest_framework.response import Response
from rest_framework.settings import api_settings
from .serializers import (UserListSerializer,
                          FileListSerializer,

                          PushListSerializer,
                          SmsListSerializer,
                          SpnListSerializer,
                          LkListSerializer,

                          CreatePushSerializer,
                          CreateSmsSerializer,
                          CreateSpnSerializer,
                          CreateLkSerializer)

class UserListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['fio']
    @swagger_auto_schema(operation_summary="This is all users", operation_description="Search example: '/users/?fio=Bob'")
    def get_queryset(self):
        obj = User.objects.all()
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        return UserListSerializer

class FileListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['path']
    @swagger_auto_schema(operation_summary="This is all log files", operation_description="Search example: '/files/?path=/home/admin/log_files/push.txt'")
    def get_queryset(self):
        obj = File.objects.all()
        return obj

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': data[api_settings.URL_FIELD_NAME]}
        except (TypeError, KeyError):
            return {}

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_class(self):
        return FileListSerializer


class PushListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'func_name', 'message', 'sequent_log', 'subsequent_log', 'project_name__name', 'user_uid__fio', 'path_name__path']
    @swagger_auto_schema(operation_summary="This is all log from push_django", operation_description="Filter example: '/all_logs/?search=lk_django'")
    def get_queryset(self):
        obj = Push.objects.all()
        return obj

    def get_serializer_class(self):
        return PushListSerializer

class SmsListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'func_name', 'message', 'sequent_log', 'subsequent_log', 'project_name__name', 'user_uid__fio', 'path_name__path']
    @swagger_auto_schema(operation_summary="This is all log from sms_django", operation_description="Filter example: '/all_logs/?search=lk_django'")
    def get_queryset(self):
        obj = Sms.objects.all()
        return obj

    def get_serializer_class(self):
        return SmsListSerializer

class SpnListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'func_name', 'message', 'sequent_log', 'subsequent_log', 'project_name__name', 'user_uid__fio', 'path_name__path']
    @swagger_auto_schema(operation_summary="This is all log from spnavigator_django", operation_description="Filter example: '/all_logs/?search=lk_django'")
    def get_queryset(self):
        obj = Spnavigator.objects.all()
        return obj

    def get_serializer_class(self):
        return SpnListSerializer

class LkListView(ListAPIView):
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'func_name', 'message', 'sequent_log', 'subsequent_log', 'project_name__name', 'user_uid__fio', 'path_name__path']
    @swagger_auto_schema(operation_summary="This is all log from lk_django", operation_description="Filter example: '/all_logs/?search=lk_django'")
    def get_queryset(self):
        obj = Lk.objects.all()
        return obj

    def get_serializer_class(self):
        return LkListSerializer



class PushPostMethod(ListCreateAPIView):
    serializer_class = CreatePushSerializer

    def perform_create(self, serializer):
        serializer.save()

class SmsPostMethod(ListCreateAPIView):
    serializer_class = CreateSmsSerializer

    def perform_create(self, serializer):
        serializer.save()

class SpnPostMethod(ListCreateAPIView):
    serializer_class = CreateSpnSerializer

    def perform_create(self, serializer):
        serializer.save()

class LkPostMethod(ListCreateAPIView):
    serializer_class = CreateLkSerializer

    def perform_create(self, serializer):
        serializer.save()