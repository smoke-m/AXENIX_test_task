# Generated by Django 4.2 on 2024-06-27 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractors',
            name='decent',
            field=models.CharField(max_length=64),
        ),
    ]
