# Generated by Django 3.0.7 on 2021-04-01 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20210327_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]