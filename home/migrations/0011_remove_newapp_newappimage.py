# Generated by Django 4.0.5 on 2022-07-05 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_newapp_newappimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newapp',
            name='newappimage',
        ),
    ]
