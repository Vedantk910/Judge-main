# Generated by Django 4.0.6 on 2022-07-19 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_testcases_problem_solution'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]