# Generated by Django 2.1.4 on 2019-03-04 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmer_details',
            name='last_name',
            field=models.CharField(default='moorthy', max_length=400, null=True),
        ),
    ]