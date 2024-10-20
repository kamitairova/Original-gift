# Generated by Django 5.1.2 on 2024-10-19 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_offer_setting_offers'),
    ]

    operations = [
        migrations.AddField(
            model_name='setting',
            name='is_active_calendars',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_active_cards',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_active_examples',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_active_manual',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_active_offers',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='setting',
            name='is_active_reviews',
            field=models.BooleanField(default=True),
        ),
    ]