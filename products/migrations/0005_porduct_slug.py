# Generated by Django 3.2.5 on 2021-09-20 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_porduct_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='porduct',
            name='slug',
            field=models.SlugField(default='undefine_slug'),
            preserve_default=False,
        ),
    ]
