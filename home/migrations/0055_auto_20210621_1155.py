# Generated by Django 3.2.3 on 2021-06-21 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0054_alter_job_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN')], max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Creative Designer', 'Creative Designer'), ('Engineering', 'Engineering')], max_length=225),
        ),
    ]
