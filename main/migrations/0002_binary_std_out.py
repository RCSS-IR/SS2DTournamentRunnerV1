# Generated by Django 4.0.4 on 2022-05-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='binary',
            name='std_out',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
