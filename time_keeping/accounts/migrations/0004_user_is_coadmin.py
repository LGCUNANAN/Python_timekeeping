# Generated by Django 4.1.5 on 2023-03-03 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_rename_check_in_time_timerecord_time_in_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_coadmin',
            field=models.BooleanField(default=False, verbose_name='Is Co-Admin'),
        ),
    ]
