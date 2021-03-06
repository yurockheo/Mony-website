# Generated by Django 3.1.7 on 2021-05-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210505_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_category',
            field=models.CharField(choices=[('C', 'Clothes'), ('F', 'Furnitures')], max_length=2),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_image',
            field=models.ImageField(upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='item_price',
            field=models.FloatField(),
        ),
    ]
