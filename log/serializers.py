from rest_framework import serializers
from .models import Push, User, File, Lk, Project, Sms, Spnavigator

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'fio')
        fields = ('__all__')

class FileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('id', 'path')

class ProjectListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name')

class PushListSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    project_name = ProjectListSerializer(read_only=True)

    class Meta:
        model = Push
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class SmsListSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    project_name = ProjectListSerializer(read_only=True)

    class Meta:
        model = Sms
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class SpnListSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    project_name = ProjectListSerializer(read_only=True)

    class Meta:
        model = Spnavigator
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class LkListSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    project_name = ProjectListSerializer(read_only=True)

    class Meta:
        model = Lk
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class CreateSpnSerializer(serializers.ModelSerializer):
    user_uid = UserListSerializer(read_only=True)
    path_name = FileListSerializer(read_only=True)
    project_name = ProjectListSerializer(read_only=True)

    class Meta:
        model = Spnavigator
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

    def create(self, validated_data):
        user_data = validated_data.pop('user_uid')
        log = Spnavigator.objects.create(**validated_data)
        for user_data in user_data:
            Spnavigator.objects.create(log=log, **user_data)
        return log