# Generated by Django 3.2.4 on 2021-07-18 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('categories', '0004_healing_knowledge_marriage_novels'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Books',
            new_name='Prayer',
        ),
    ]
