# Generated by Django 3.1.6 on 2021-02-14 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_delete_login'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Users',
        ),
    ]