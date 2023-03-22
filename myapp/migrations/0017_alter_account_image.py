# Generated by Django 4.1.7 on 2023-03-19 08:39

from django.db import migrations, models
import myapp.storage


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_alter_account_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=models.ImageField(max_length=25000, null=True, storage=myapp.storage.OverwriteStorage(), upload_to='Media'),
        ),
    ]