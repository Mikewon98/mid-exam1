# Generated by Django 4.1.4 on 2022-12-23 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='studentName',
            new_name='studentname',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(max_length=100),
        ),
    ]
