# Generated by Django 3.2.3 on 2021-06-18 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0047_auto_20210618_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=15)),
                ('amount', models.FloatField()),
            ],
        ),
    ]
