# Generated by Django 3.2.6 on 2021-08-18 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='logIn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
            ],
        ),
        migrations.CreateModel(
            name='signUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='username')),
                ('password', models.CharField(max_length=200, verbose_name='password')),
                ('confirm_password', models.CharField(max_length=200, verbose_name='confirm_password')),
            ],
        ),
    ]
