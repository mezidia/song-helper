# Generated by Django 3.1.8 on 2021-07-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mesite', '0002_auto_20210312_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mood',
            name='mood',
            field=models.CharField(choices=[('happy', 'Happy'), ('energetic', 'Energetic'), ('calm', 'Calm'), ('sad', 'Sad')], max_length=15),
        ),
    ]
