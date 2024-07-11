# Generated by Django 5.0.7 on 2024-07-11 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_product_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_surname', models.CharField(blank=True, max_length=200, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]