# Generated by Django 5.0.6 on 2024-07-09 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=200, null=True)),
                ('product_description', models.TextField(blank=True, max_length=1000, null=True)),
                ('product_week', models.IntegerField(blank=True, null=True)),
                ('product_hours', models.FloatField(blank=True, null=True)),
                ('product_price', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='product/')),
            ],
        ),
    ]
