# Generated by Django 4.1.7 on 2023-03-13 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_followers_followings_delete_img_account_connect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followings',
            name='usernam',
            field=models.TextField(null=True),
        ),
    ]
