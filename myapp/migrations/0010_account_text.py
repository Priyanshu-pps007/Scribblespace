# Generated by Django 4.1.7 on 2023-03-13 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_account_image_alter_account_followers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='text',
            field=models.CharField(default='', max_length=1000, null=True),
        ),
    ]
