# Generated by Django 5.1.2 on 2024-10-30 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='outstanding',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]