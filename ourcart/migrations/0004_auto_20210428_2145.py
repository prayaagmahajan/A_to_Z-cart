# Generated by Django 3.1.7 on 2021-04-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourcart', '0003_auto_20210428_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='desc',
            field=models.CharField(max_length=4000),
        ),
    ]
