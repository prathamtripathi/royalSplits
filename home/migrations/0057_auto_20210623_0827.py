# Generated by Django 3.2.3 on 2021-06-23 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0056_auto_20210621_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Job1', 'Job1'), ('Creative Designer', 'Creative Designer'), ('Job4', 'Job3'), ('Finance', 'Finance'), ('Job2', 'Job2'), ('Engineering', 'Engineering')], max_length=225),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]