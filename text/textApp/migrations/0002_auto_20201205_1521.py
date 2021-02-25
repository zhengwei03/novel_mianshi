# Generated by Django 2.0 on 2020-12-05 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_vip',
            field=models.CharField(choices=[('1', '普通用户'), ('2', '会员')], default=1, max_length=6, verbose_name='是否是会员'),
        ),
    ]
