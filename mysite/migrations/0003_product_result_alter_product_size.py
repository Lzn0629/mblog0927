# Generated by Django 4.2.4 on 2023-11-01 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='result',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=1),
        ),
    ]
