# Generated by Django 2.2 on 2019-07-20 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_config', '0004_auto_20190720_1642'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='menu_name',
            new_name='authority',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='is_menu',
            new_name='authorityId',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_power',
            new_name='authorityName',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='parent_id',
            new_name='isMenu',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='menu_url',
            new_name='menuUrl',
        ),
        migrations.AddField(
            model_name='menu',
            name='orderNumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='parentId',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]