# Generated by Django 4.0.3 on 2022-07-12 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='desription',
            new_name='description',
        ),
    ]
