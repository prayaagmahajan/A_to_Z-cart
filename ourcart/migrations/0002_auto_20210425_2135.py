# Generated by Django 3.1.7 on 2021-04-25 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourcart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='banner/images')),
                ('heading', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='ourcart/images'),
        ),
    ]
