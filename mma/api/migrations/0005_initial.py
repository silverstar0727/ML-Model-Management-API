# Generated by Django 4.0 on 2021-12-20 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0004_delete_models_delete_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=30)),
                ('description', models.CharField(default='', max_length=200)),
                ('created_datetime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='Models',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=30)),
                ('description', models.CharField(default='', max_length=100)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.project')),
            ],
            options={
                'db_table': 'models',
            },
        ),
    ]