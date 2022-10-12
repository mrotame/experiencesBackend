# Generated by Django 4.1.2 on 2022-10-12 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiencias', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experiencias',
            options={'permissions': (('can_undelete', 'Can undelete this object'),)},
        ),
        migrations.AddField(
            model_name='experiencias',
            name='deleted_at',
            field=models.DateTimeField(blank=True, db_index=True, default=None, editable=False, null=True),
        ),
    ]