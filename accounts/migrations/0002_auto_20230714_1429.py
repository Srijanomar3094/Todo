# Generated by Django 2.0 on 2023-07-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='val',
            field=models.IntegerField(default=0),
        ),
    ]
