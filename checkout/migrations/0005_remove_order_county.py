# Generated by Django 3.0.8 on 2020-09-16 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_order_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='county',
        ),
    ]
