# Generated by Django 4.0.5 on 2022-07-12 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0024_addexam_newexamtime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addexam',
            name='examnewapp',
        ),
    ]
