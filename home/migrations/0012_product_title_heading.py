# Generated by Django 3.2.3 on 2021-06-06 11:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210606_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='title_heading',
            field=models.CharField(default=django.utils.timezone.now, max_length=225),
            preserve_default=False,
        ),
    ]