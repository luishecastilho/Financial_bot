# Generated by Django 4.1.5 on 2023-01-17 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='order',
        ),
        migrations.AddField(
            model_name='video',
            name='sim',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
