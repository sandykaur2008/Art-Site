# Generated by Django 2.0.6 on 2018-06-21 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20180621_2335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='piece',
            name='delete',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
    ]
