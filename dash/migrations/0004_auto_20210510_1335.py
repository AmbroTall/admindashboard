# Generated by Django 3.2.2 on 2021-05-10 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dash', '0003_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
