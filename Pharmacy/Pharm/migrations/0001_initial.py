# Generated by Django 4.1 on 2023-09-22 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pharmacy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('services', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=500)),
                ('location', models.CharField(max_length=200)),
                ('founder', models.CharField(max_length=500)),
                ('facebook', models.CharField(max_length=500)),
                ('twitter', models.CharField(max_length=500)),
                ('instagram', models.CharField(max_length=500)),
                ('phoneNumber', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('About', models.TextField()),
                ('logo', models.FileField(upload_to='Pharmacy_logo')),
                ('image1', models.FileField(upload_to='PharmacyImage')),
                ('image2', models.FileField(upload_to='PharmacyImage')),
            ],
            options={
                'verbose_name_plural': 'Pharmacy',
            },
        ),
    ]
