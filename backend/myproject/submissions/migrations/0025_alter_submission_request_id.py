# Generated by Django 5.0.6 on 2024-05-31 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0024_alter_submission_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='request_id',
            field=models.CharField(default='03664e7f7b4e45308caa56a35c5716aa', max_length=100, unique=True),
        ),
    ]
