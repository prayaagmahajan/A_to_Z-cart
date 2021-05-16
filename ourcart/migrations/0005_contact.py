# Generated by Django 3.1.7 on 2021-05-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourcart', '0004_auto_20210428_2145'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(default='', max_length=70)),
                ('phone', models.CharField(default='', max_length=70)),
                ('desc', models.CharField(default='', max_length=500)),
            ],
        ),
    ]
