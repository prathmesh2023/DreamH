# Generated by Django 3.2.3 on 2021-06-04 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0021_delete_brands'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimg',
            field=models.ImageField(default='', height_field='600', upload_to='shop1/images', width_field='300'),
        ),
    ]