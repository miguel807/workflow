# Generated by Django 3.0 on 2023-12-06 18:29

from django.db import migrations, models
import django.db.models.deletion
import river.models.fields.state


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('river', '0002_auto_20231204_1716'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('term', models.CharField(max_length=30)),
                ('grade', models.IntegerField(default=1)),
                ('attempt', models.IntegerField(default=0)),
                ('student_state_field', river.models.fields.state.StateField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='river.State')),
            ],
            options={
                'verbose_name': 'EstudentModel',
                'verbose_name_plural': 'EstudentModels',
            },
        ),
    ]
