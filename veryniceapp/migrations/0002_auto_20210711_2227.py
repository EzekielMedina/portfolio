# Generated by Django 2.2 on 2021-07-11 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veryniceapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='usermessage',
            field=models.CharField(max_length=55),
        ),
    ]
