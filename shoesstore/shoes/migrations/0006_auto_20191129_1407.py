# Generated by Django 2.2.6 on 2019-11-29 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0005_auto_20191129_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='shoes/media '),
        ),
    ]
