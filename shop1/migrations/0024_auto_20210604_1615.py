# Generated by Django 3.2.3 on 2021-06-04 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0023_auto_20210604_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pimg',
            field=models.ImageField(default='', height_field='600', upload_to='shop1/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimg2',
            field=models.ImageField(default=1, height_field='600', upload_to='shop1/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimg3',
            field=models.ImageField(default=1, height_field='600', upload_to='shop1/images'),
        ),
    ]
