# Generated by Django 2.0.7 on 2018-08-01 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20180801_2055'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='titl_x_e',
            new_name='title',
        ),
    ]
