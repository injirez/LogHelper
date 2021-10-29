from django.db import models
import uuid

class Push(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_uid = models.ForeignKey('User', on_delete=models.CASCADE, default=uuid.uuid4)
    path_name = models.ForeignKey('File', on_delete=models.CASCADE, default=uuid.uuid4)
    func_name = models.CharField('Name of function', max_length=50)
    message = models.CharField('Message of log', max_length=300)
    sequent_log = models.UUIDField(default=uuid.uuid4)
    subsequent_log = models.UUIDField(default=uuid.uuid4)

class Sms(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_uid = models.ForeignKey('User', on_delete=models.CASCADE, default=uuid.uuid4)
    path_name = models.ForeignKey('File', on_delete=models.CASCADE, default=uuid.uuid4)
    func_name = models.CharField('Name of function', max_length=50)
    message = models.CharField('Message of log', max_length=300)
    sequent_log = models.UUIDField(default=uuid.uuid4)
    subsequent_log = models.UUIDField(default=uuid.uuid4)
#
class Spnavigator(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_uid = models.ForeignKey('User', on_delete=models.CASCADE, default=uuid.uuid4)
    path_name = models.ForeignKey('File', on_delete=models.CASCADE, default=uuid.uuid4)
    func_name = models.CharField('Name of function', max_length=50)
    message = models.CharField('Message of log', max_length=300)
    sequent_log = models.UUIDField(default=uuid.uuid4)
    subsequent_log = models.UUIDField(default=uuid.uuid4)

class Lk(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user_uid = models.ForeignKey('User', on_delete=models.CASCADE, default=uuid.uuid4)
    path_name = models.ForeignKey('File', on_delete=models.CASCADE, default=uuid.uuid4)
    func_name = models.CharField('Name of function', max_length=50)
    message = models.CharField('Message of log', max_length=300)
    sequent_log = models.UUIDField(default=uuid.uuid4)
    subsequent_log = models.UUIDField(default=uuid.uuid4)

class User(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    fio = models.CharField('Fio of user', max_length=150)

class File(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    path = models.CharField('Path to log file', max_length=500, unique=True)

