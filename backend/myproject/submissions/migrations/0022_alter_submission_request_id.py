# Generated by Django 5.0.6 on 2024-05-30 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0021_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='d1c779be9c5f4bf595b2dc1e2887e330', max_length=100, unique=True),
        ),
    ]
