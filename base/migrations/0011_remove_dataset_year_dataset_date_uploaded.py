# Generated by Django 4.2.5 on 2023-11-29 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_dataset_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='year',
        ),
        migrations.AddField(
            model_name='dataset',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]