# Generated by Django 4.1.7 on 2023-03-21 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_upimages_dislike_count_upimages_like_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upimages',
            name='dislike_count',
            field=models.IntegerField(max_length=20000, null=True),
        ),
        migrations.AlterField(
            model_name='upimages',
            name='like_count',
            field=models.IntegerField(max_length=20000, null=True),
        ),
    ]
