# Generated by Django 2.2 on 2019-07-20 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0006_auto_20190720_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='authority',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menuIcon',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menuUrl',
            field=models.CharField(max_length=100),
        ),
    ]