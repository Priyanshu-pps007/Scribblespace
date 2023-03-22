# Generated by Django 4.1.7 on 2023-03-21 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0027_upimages_dislike_count_upimages_like_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='dislike',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='disliked_by', to='myapp.upimages'),
        ),
        migrations.AddField(
            model_name='account',
            name='like',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='liked_by', to='myapp.upimages'),
        ),
    ]
