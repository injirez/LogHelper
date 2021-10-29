from rest_framework import serializers
from .models import Push, User, File

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'fio')

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'path')


class PushListSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    class Meta:
        model = Push
        fields = ('id', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')