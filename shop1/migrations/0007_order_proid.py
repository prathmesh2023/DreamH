# Generated by Django 3.1 on 2020-08-22 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop1', '0006_auto_20200818_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='proid',
            field=models.CharField(default='', max_length=50, verbose_name='proid'),
        ),
    ]
