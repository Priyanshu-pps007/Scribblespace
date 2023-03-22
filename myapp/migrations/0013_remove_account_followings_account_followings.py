# Generated by Django 4.1.7 on 2023-03-14 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_remove_account_followers_account_followers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='followings',
        ),
        migrations.AddField(
            model_name='account',
            name='followings',
            field=models.ManyToManyField(blank=True, related_name='folloing_by', to='myapp.account'),
        ),
    ]
