# from django.http import HttpResponse, JsonResponse

from .models import Push, Sms, User, File, Spnavigator, Lk
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from .serializers import UserListSerializer, FileListSerializer, PushListSerializer

# def get_push(request):
#     res = []
#     obj = list(Push.objects.all())
#
#     # print(obj[0].user_uid)
#
#     for data in list(Push.objects.select_related()):
#         res.append({'id': data.id, 'user_uid': str(data.user_uid), 'func_name': data.func_name, 'message': data.message, 'sequent_log': data.sequent_log, 'subsequent_log': data.subsequent_log})
#     return JsonResponse(res, safe=False)

class UserListView(APIView):
    @swagger_auto_schema(operation_summary="This is all users")
    def get(self, request):
        obj = User.objects.all()
        serializer = UserListSerializer(obj, many=True)

        return Response(serializer.data)

class FileListView(APIView):
    @swagger_auto_schema(operation_summary="This is all log files")
    def get(self, request):
        obj = File.objects.all()
        serializer = FileListSerializer(obj, many=True)

        return Response(serializer.data)

class PushListView(APIView):
    @swagger_auto_schema(operation_summary="This is all log push")
    def get(self, request):
        obj = Push.objects.all()
        serializer = PushListSerializer(obj, many=True)

        return Response(serializer.data)


