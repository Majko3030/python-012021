# Generated by Django 3.2 on 2021-04-20 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('ico', models.CharField(max_length=100)),
                ('ulice', models.CharField(max_length=100)),
                ('psc', models.CharField(max_length=100)),
                ('mesto', models.CharField(max_length=100)),
            ],
        ),
    ]