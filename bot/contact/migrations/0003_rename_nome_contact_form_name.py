# Generated by Django 4.1.5 on 2023-01-12 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contact_form_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact_form',
            old_name='nome',
            new_name='name',
        ),
    ]
