# Generated by Django 5.0.3 on 2024-03-23 21:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0008_todo_due_date_modified_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateTimeField(verbose_name=django.utils.timezone.now),
        ),
    ]
