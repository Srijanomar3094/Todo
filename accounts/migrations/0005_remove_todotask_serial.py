# Generated by Django 2.0 on 2023-07-16 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230714_1456'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todotask',
            name='serial',
        ),
    ]
