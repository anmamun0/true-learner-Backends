# Generated by Django 5.0.7 on 2025-03-25 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studenthistory',
            options={'ordering': ['-created_on']},
        ),
    ]
