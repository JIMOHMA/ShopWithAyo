# Generated by Django 2.0.7 on 2021-02-06 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_category', '0004_auto_20210206_0616'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
