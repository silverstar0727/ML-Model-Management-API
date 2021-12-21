# Generated by Django 4.0 on 2021-12-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Experiments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parameters', models.JSONField()),
                ('training_data_path', models.CharField(max_length=255)),
                ('validation_data_path', models.CharField(max_length=255)),
                ('test_data_path', models.CharField(max_length=255)),
                ('evaluation', models.FloatField(null=True)),
                ('artifact_file_path', models.CharField(max_length=255, null=True)),
                ('model_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.models')),
            ],
            options={
                'db_table': 'experiments',
            },
        ),
    ]
