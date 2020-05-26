# Generated by Django 3.0.2 on 2020-01-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mydata',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='mydata',
            name='name',
        ),
        migrations.AddField(
            model_name='mydata',
            name='Email',
            field=models.CharField(default='abc@gmail.com', max_length=30),
        ),
        migrations.AddField(
            model_name='mydata',
            name='Gender',
            field=models.CharField(default='Male', max_length=15),
        ),
        migrations.AddField(
            model_name='mydata',
            name='Last_Name',
            field=models.CharField(default='Xyz', max_length=30),
        ),
        migrations.AddField(
            model_name='mydata',
            name='Name',
            field=models.CharField(default='Abc', max_length=30),
        ),
    ]
