# Generated by Django 3.2 on 2021-05-02 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0002_auto_20210502_2322'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('prijmeni', models.CharField(max_length=100)),
                ('cislo_ridicského_prukazu', models.CharField(max_length=100)),
                ('datum_narozeni', models.DateTimeField()),
            ],
        ),
    ]
