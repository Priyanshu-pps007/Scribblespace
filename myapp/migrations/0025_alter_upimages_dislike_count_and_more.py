# Generated by Django 4.1.7 on 2023-03-21 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0024_alter_upimages_dislike_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upimages',
            name='dislike_count',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='upimages',
            name='like_count',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
