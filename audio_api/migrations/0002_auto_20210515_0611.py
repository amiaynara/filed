# Generated by Django 3.2.3 on 2021-05-15 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
