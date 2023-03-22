# Generated by Django 4.1.7 on 2023-03-13 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_account_connect_remove_account_connecting_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='image',
            field=models.ImageField(null=True, upload_to='Media'),
        ),
        migrations.AlterField(
            model_name='account',
            name='followers',
            field=models.FileField(null=True, upload_to='Media'),
        ),
        migrations.AlterField(
            model_name='account',
            name='followings',
            field=models.FileField(null=True, upload_to='Media'),
        ),
    ]