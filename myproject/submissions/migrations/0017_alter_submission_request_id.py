# Generated by Django 5.0.6 on 2024-05-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0016_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='5d8173afabc8473c8793140de58d78f2', max_length=100, unique=True),
        ),
    ]
