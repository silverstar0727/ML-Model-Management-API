# Generated by Django 4.0 on 2021-12-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_experiments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experiments',
            name='parameters',
            field=models.TextField(),
        ),
    ]
