# Generated by Django 2.2 on 2019-04-17 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testDjango_app', '0004_auto_20190416_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='image',
            field=models.ImageField(null=True, upload_to='image'),
        ),
    ]
