# Generated by Django 5.0.6 on 2024-10-20 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tejapp', '0004_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='imglink',
            field=models.CharField(default='/static/blackprog.jpg', max_length=50),
        ),
    ]
