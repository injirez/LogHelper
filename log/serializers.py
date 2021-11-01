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




class CreatePushSerializer(serializers.ModelSerializer):
    user_uid = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='fio')
    path_name = serializers.SlugRelatedField(queryset=File.objects.all(), slug_field='path')
    project_name = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Push
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class CreateSmsSerializer(serializers.ModelSerializer):
    user_uid = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='fio')
    path_name = serializers.SlugRelatedField(queryset=File.objects.all(), slug_field='path')
    project_name = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Sms
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class CreateSpnSerializer(serializers.ModelSerializer):
    user_uid = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='fio')
    path_name = serializers.SlugRelatedField(queryset=File.objects.all(), slug_field='path')
    project_name = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Spnavigator
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')

class CreateLkSerializer(serializers.ModelSerializer):
    user_uid = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='fio')
    path_name = serializers.SlugRelatedField(queryset=File.objects.all(), slug_field='path')
    project_name = serializers.SlugRelatedField(queryset=Project.objects.all(), slug_field='name')

    class Meta:
        model = Lk
        fields = ('id', 'project_name', 'user_uid', 'path_name', 'func_name', 'message', 'sequent_log', 'subsequent_log')
