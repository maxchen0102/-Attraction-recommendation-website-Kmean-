# Generated by Django 3.2.3 on 2022-10-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pic_label', models.IntegerField(default=0)),
                ('pic_name', models.CharField(default='', max_length=100)),
                ('pic_intro', models.CharField(default='', max_length=100)),
                ('pic_link', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ProductModel',
        ),
    ]
