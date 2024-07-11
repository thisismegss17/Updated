# Generated by Django 5.0.7 on 2024-07-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kategori',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kategori_name', models.CharField(blank=True, max_length=300, null=True)),
                ('kategori_image', models.ImageField(blank=True, null=True, upload_to='about/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_hours',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_week',
        ),
    ]
