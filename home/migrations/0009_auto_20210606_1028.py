# Generated by Django 3.2.3 on 2021-06-06 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210606_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail_3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail_4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
