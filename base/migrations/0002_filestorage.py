# Generated by Django 4.1.2 on 2022-10-29 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Filestorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_Name', models.FileField(default='images.png', null=True, upload_to='')),
            ],
        ),
    ]
