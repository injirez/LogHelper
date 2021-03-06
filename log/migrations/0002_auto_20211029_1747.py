# Generated by Django 3.2.8 on 2021-10-29 17:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='id',
        ),
        migrations.RemoveField(
            model_name='lk',
            name='id',
        ),
        migrations.RemoveField(
            model_name='push',
            name='id',
        ),
        migrations.RemoveField(
            model_name='sms',
            name='id',
        ),
        migrations.RemoveField(
            model_name='spnavigator',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AlterField(
            model_name='file',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='lk',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='push',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sms',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='spnavigator',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='idd',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
