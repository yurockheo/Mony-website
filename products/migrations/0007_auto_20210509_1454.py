# Generated by Django 3.1.7 on 2021-05-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210509_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_image',
            field=models.FilePathField(path='static/images'),
        ),
    ]
