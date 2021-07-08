# Generated by Django 3.2.3 on 2021-06-21 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0052_auto_20210619_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='title',
            field=models.CharField(choices=[('Engineering', 'Engineering'), ('Finance', 'Finance'), ('Creative Designer', 'Creative Designer')], max_length=225),
        ),
    ]