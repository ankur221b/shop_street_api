# Generated by Django 4.2.2 on 2023-06-30 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Price',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]