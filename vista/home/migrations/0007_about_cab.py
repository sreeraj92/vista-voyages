# Generated by Django 5.1.1 on 2024-12-16 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_driver_registration_roles'),
    ]

    operations = [
        migrations.CreateModel(
            name='about_cab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cab_Type', models.CharField(max_length=100, null=True)),
                ('Make_Model', models.CharField(max_length=100, null=True)),
                ('Registration_Number', models.CharField(max_length=177, null=True)),
                ('Color', models.CharField(max_length=98, null=True)),
                ('vehicle_image', models.ImageField(null=True, upload_to='cabimg')),
                ('Driver_Name', models.CharField(max_length=234, null=True)),
                ('Driver_Contact', models.CharField(max_length=345, null=True)),
                ('Seating_Capacity', models.CharField(max_length=90, null=True)),
                ('Base_Fare', models.CharField(max_length=342, null=True)),
                ('Fare_per_Kilometer', models.CharField(max_length=456, null=True)),
                ('Safety_Features', models.CharField(max_length=700, null=True)),
                ('Availability', models.CharField(max_length=780, null=True)),
            ],
        ),
    ]