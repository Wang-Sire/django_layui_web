# Generated by Django 2.2 on 2019-07-20 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(max_length=100)),
                ('menu_icon', models.CharField(max_length=100)),
                ('menu_url', models.CharField(max_length=20)),
                ('parent_id', models.IntegerField()),
                ('is_menu', models.IntegerField()),
            ],
            options={
                'verbose_name': '菜单管理',
                'verbose_name_plural': '菜单管理',
            },
        ),
    ]