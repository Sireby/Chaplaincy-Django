# Generated by Django 3.2.4 on 2021-07-18 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
        ('categories', '0005_rename_books_prayer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('coverImage', models.FileField(blank=True, null=True, upload_to='')),
                ('bookFile', models.FileField(blank=True, null=True, upload_to='')),
                ('description', models.CharField(max_length=255)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Account.usertable')),
            ],
        ),
    ]
