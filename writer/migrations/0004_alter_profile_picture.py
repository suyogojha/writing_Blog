# Generated by Django 3.2.8 on 2021-11-01 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writer', '0003_auto_20211101_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='img/default.jpg', null=True, upload_to='img'),
        ),
    ]