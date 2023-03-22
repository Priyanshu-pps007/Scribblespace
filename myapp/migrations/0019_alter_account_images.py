# Generated by Django 4.1.7 on 2023-03-19 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_image_remove_account_image_account_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='images',
            field=models.ManyToManyField(blank=True, related_name='image', to='myapp.account'),
        ),
    ]
