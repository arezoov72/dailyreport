# Generated by Django 3.1.2 on 2021-06-15 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailyreport', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reportdetails',
            name='undonework',
            field=models.TextField(null=True),
        ),
    ]
