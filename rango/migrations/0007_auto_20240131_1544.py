# Generated by Django 2.1.5 on 2024-01-31 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0006_page_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'verbose_name_plural': 'pages'},
        ),
    ]