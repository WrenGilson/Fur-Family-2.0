# Generated by Django 4.1.2 on 2022-10-05 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='animalType',
            field=models.CharField(default='type', max_length=200),
        ),
    ]
