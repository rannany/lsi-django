# Generated by Django 2.0.5 on 2018-05-20 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0007_auto_20180514_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='adverb_verb',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='document',
            name='stopwords',
            field=models.IntegerField(default=0),
        ),
    ]
