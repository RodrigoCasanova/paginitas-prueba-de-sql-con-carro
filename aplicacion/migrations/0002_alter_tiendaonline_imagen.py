# Generated by Django 5.0.6 on 2024-06-03 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tiendaonline',
            name='imagen',
            field=models.ImageField(null=True, upload_to='personas'),
        ),
    ]
