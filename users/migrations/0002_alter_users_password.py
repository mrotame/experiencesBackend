# Generated by Django 4.1.2 on 2022-10-11 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=256, verbose_name="User's password"),
        ),
    ]
