# Generated by Django 4.2.2 on 2023-07-02 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
