# Generated by Django 2.2.2 on 2019-06-22 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_position_currenttoken'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='position',
            options={'ordering': ['lastupdate']},
        ),
    ]
