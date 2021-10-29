# Generated by Django 3.2.8 on 2021-10-29 17:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_auto_20211029_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='lk',
            name='path_name',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.file'),
        ),
        migrations.AddField(
            model_name='lk',
            name='user_uid',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.user'),
        ),
        migrations.AddField(
            model_name='push',
            name='path_name',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.file'),
        ),
        migrations.AddField(
            model_name='push',
            name='user_uid',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.user'),
        ),
        migrations.AddField(
            model_name='sms',
            name='path_name',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.file'),
        ),
        migrations.AddField(
            model_name='sms',
            name='user_uid',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.user'),
        ),
        migrations.AddField(
            model_name='spnavigator',
            name='path_name',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.file'),
        ),
        migrations.AddField(
            model_name='spnavigator',
            name='user_uid',
            field=models.ForeignKey(default=uuid.uuid4, on_delete=django.db.models.deletion.CASCADE, to='log.user'),
        ),
    ]