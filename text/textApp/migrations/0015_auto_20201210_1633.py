# Generated by Django 2.0.1 on 2020-12-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('textApp', '0014_bookchapter_chapter_types'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookchapter',
            name='chapter_types',
            field=models.CharField(choices=[(1, '免费'), (2, '会员')], max_length=5),
        ),
    ]
