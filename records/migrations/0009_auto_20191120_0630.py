# Generated by Django 2.2.4 on 2019-11-20 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0008_auto_20191120_0548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomments',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]