# Generated by Django 2.0 on 2018-01-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0014_vacancytest_max_attempts'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatevacancypassing',
            name='passed',
            field=models.BooleanField(default=False),
        ),
    ]