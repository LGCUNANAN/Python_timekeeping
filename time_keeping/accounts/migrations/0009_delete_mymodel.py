# Generated by Django 4.1.5 on 2023-03-09 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_mymodel_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
    ]