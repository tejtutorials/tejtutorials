# Generated by Django 5.0.6 on 2024-10-20 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('batch', models.CharField(max_length=50)),
                ('percentage', models.CharField(max_length=50)),
                ('imglink', models.CharField(db_default='/static/blackprog.jpg', max_length=50)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
    ]
