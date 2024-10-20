# Generated by Django 5.1.2 on 2024-10-20 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_card_list_1_alter_card_list_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image',
            field=models.ImageField(blank=True, help_text='Выберите изображение для карточки', null=True, upload_to='CardIco'),
        ),
        migrations.AlterField(
            model_name='example',
            name='is_active_2',
            field=models.BooleanField(default=False),
        ),
    ]
