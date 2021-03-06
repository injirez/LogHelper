# Generated by Django 3.2.8 on 2021-10-29 17:46

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('path', models.CharField(max_length=500, unique=True, verbose_name='Path to log file')),
            ],
        ),
        migrations.CreateModel(
            name='Lk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('func_name', models.CharField(max_length=50, verbose_name='Name of function')),
                ('message', models.CharField(max_length=300, verbose_name='Message of log')),
                ('sequent_log', models.UUIDField(default=uuid.uuid4)),
                ('subsequent_log', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='Push',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('func_name', models.CharField(max_length=50, verbose_name='Name of function')),
                ('message', models.CharField(max_length=300, verbose_name='Message of log')),
                ('sequent_log', models.UUIDField(default=uuid.uuid4)),
                ('subsequent_log', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='Sms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('func_name', models.CharField(max_length=50, verbose_name='Name of function')),
                ('message', models.CharField(max_length=300, verbose_name='Message of log')),
                ('sequent_log', models.UUIDField(default=uuid.uuid4)),
                ('subsequent_log', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='Spnavigator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('func_name', models.CharField(max_length=50, verbose_name='Name of function')),
                ('message', models.CharField(max_length=300, verbose_name='Message of log')),
                ('sequent_log', models.UUIDField(default=uuid.uuid4)),
                ('subsequent_log', models.UUIDField(default=uuid.uuid4)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idd', models.UUIDField(default=uuid.uuid4)),
                ('fio', models.CharField(max_length=150, verbose_name='Fio of user')),
            ],
        ),
    ]
