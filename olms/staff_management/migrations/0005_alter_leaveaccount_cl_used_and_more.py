# Generated by Django 4.2.20 on 2025-04-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff_management', '0004_leaveaccount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaveaccount',
            name='cl_used',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='leaveaccount',
            name='el_used',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='leaveaccount',
            name='sl_used',
            field=models.IntegerField(null=True),
        ),
    ]
