# Generated by Django 4.0.5 on 2022-07-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newapp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('newappname', models.CharField(max_length=122)),
                ('newappemail', models.CharField(max_length=122)),
                ('newappphone', models.CharField(max_length=12)),
                ('newappaddress', models.CharField(max_length=122)),
                ('newappdepart', models.CharField(max_length=122)),
            ],
        ),
    ]
