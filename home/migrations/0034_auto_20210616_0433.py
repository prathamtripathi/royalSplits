# Generated by Django 3.2.3 on 2021-06-16 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0033_auto_20210615_1912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Creative Designer', 'Creative Designer'), ('Engineering', 'Engineering')], max_length=225),
        ),
        migrations.AlterField(
            model_name='jobapplication',
            name='resume',
            field=models.FileField(upload_to=''),
        ),
    ]
