# Generated by Django 5.0.6 on 2024-05-23 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0004_alter_submission_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='02ff0e7a7d2c4a37a3230cf4f44a5669', max_length=100, unique=True),
        ),
    ]
