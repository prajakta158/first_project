# Generated by Django 4.1.4 on 2023-04-15 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]