# Generated by Django 2.0 on 2018-01-30 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0006_auto_20180130_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]