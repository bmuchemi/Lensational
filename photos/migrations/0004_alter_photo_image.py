# Generated by Django 4.0.5 on 2022-06-01 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20220601_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
