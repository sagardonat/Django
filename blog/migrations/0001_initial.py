# Generated by Django 5.0.6 on 2024-05-14 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auther', models.CharField(max_length=150)),
                ('title', models.CharField(max_length=450)),
                ('description', models.TextField()),
            ],
        ),
    ]
