# Generated by Django 5.0.6 on 2024-05-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('ca_id', models.AutoField(primary_key=True, serialize=False)),
                ('ca_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post_title', models.CharField(max_length=45)),
                ('post_content', models.CharField(max_length=45)),
                ('created_at', models.DateTimeField()),
                ('post_img', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
    ]