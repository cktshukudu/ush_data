# Generated by Django 4.1.2 on 2022-10-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='No name', max_length=45)),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('price', models.FloatField(default=0)),
                ('descript', models.CharField(max_length=30)),
                ('avater', models.ImageField(default='images.png', null=True, upload_to='')),
            ],
        ),
    ]
