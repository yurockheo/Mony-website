# Generated by Django 3.1.7 on 2021-05-09 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20210508_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]