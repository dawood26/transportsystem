# Generated by Django 2.1.1 on 2018-09-06 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0002_customuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
