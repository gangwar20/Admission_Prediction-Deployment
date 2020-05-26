# Generated by Django 2.2.7 on 2020-01-22 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('Mobile', models.IntegerField()),
                ('gender', models.CharField(max_length=15)),
                ('TOFEL', models.IntegerField()),
                ('GRE', models.IntegerField()),
                ('UNI_rating', models.IntegerField()),
                ('SOP', models.IntegerField()),
                ('LOR', models.IntegerField()),
                ('CGPA', models.IntegerField()),
                ('Research_Ex', models.IntegerField()),
            ],
        ),
    ]