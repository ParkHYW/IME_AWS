# Generated by Django 4.0.1 on 2022-05-24 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cities', '0004_anthropometry_computer_cost'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Cost',
            new_name='Distribution',
        ),
    ]
