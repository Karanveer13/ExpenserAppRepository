# Generated by Django 4.0.2 on 2022-03-09 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('splitter', '0003_rename_friends_group_group_friends'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='group_friends',
            new_name='friends',
        ),
    ]
