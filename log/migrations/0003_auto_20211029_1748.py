# Generated by Django 3.2.8 on 2021-10-29 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_auto_20211029_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='idd',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='lk',
            old_name='idd',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='push',
            old_name='idd',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='sms',
            old_name='idd',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='spnavigator',
            old_name='idd',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='idd',
            new_name='id',
        ),
    ]