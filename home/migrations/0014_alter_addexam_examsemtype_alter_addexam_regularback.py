# Generated by Django 4.0.5 on 2022-07-07 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_alter_addexam_examdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addexam',
            name='examsemtype',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='addexam',
            name='regularback',
            field=models.CharField(blank=True, max_length=122, null=True),
        ),
    ]