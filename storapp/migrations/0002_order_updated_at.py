# Generated by Django 4.2.4 on 2023-08-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
