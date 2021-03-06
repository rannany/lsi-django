# Generated by Django 2.0.5 on 2018-05-14 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('documentos', '0003_auto_20180514_0136'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTerm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField()),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.Document')),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term', models.CharField(max_length=255, unique=True)),
                ('frequency', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='documentterm',
            name='term',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='documentos.Term'),
        ),
        migrations.AddField(
            model_name='document',
            name='terms',
            field=models.ManyToManyField(through='documentos.DocumentTerm', to='documentos.Term'),
        ),
    ]
