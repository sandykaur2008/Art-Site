# Generated by Django 2.0.6 on 2018-06-22 00:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20180621_2344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='delete',
            new_name='delete_piece',
        ),
    ]