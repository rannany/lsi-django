# Generated by Django 2.0.5 on 2018-05-14 01:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0002_auto_20180511_1844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documentterm',
            name='document',
        ),
        migrations.DeleteModel(
            name='Term',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='url',
            new_name='file',
        ),
        migrations.AddField(
            model_name='document',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='DocumentTerm',
        ),
    ]
