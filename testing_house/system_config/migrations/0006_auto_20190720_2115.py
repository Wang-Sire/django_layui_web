# Generated by Django 2.2 on 2019-07-20 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0005_auto_20190720_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='authority',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menuIcon',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menuUrl',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
