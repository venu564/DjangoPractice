# Generated by Django 4.2.20 on 2025-04-15 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_management', '0002_faculty_staff_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leaves',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_type', models.CharField(max_length=10)),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
                ('comments', models.CharField(max_length=1000)),
            ],
        ),
    ]
