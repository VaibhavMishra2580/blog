# Generated by Django 2.2.4 on 2019-12-04 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0010_blogdetails_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogdetails',
            name='created_at',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
