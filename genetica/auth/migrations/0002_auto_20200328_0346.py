# Generated by Django 3.0.4 on 2020-03-28 03:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('genetica_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_id',
            new_name='id',
        ),
    ]
