# Generated by Django 5.0.6 on 2024-10-20 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tejapp', '0012_moment_uniqueid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moment',
            old_name='link',
            new_name='linkforvideo',
        ),
    ]