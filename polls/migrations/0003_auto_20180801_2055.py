# Generated by Django 2.0.7 on 2018-08-01 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='titl_x_e',
        ),
    ]