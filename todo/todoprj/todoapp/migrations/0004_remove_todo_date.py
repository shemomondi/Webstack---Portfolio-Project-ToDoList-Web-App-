# Generated by Django 5.0.3 on 2024-03-20 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_todo_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='date',
        ),
    ]
