# Generated by Django 3.0.7 on 2021-03-22 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_product_specification'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
