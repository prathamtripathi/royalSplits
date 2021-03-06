# Generated by Django 3.2.3 on 2021-07-04 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0067_alter_job_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Finance', 'Finance'), ('Job2', 'Job2'), ('Job1', 'Job1'), ('Engineering', 'Engineering'), ('Creative Designer', 'Creative Designer'), ('Job3', 'Job3')], max_length=225),
        ),
    ]
