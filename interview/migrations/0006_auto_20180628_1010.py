# Generated by Django 2.0.3 on 2018-06-28 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobboard', '0001_initial'),
        ('interview', '0005_auto_20180628_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewpassed',
            name='candidate',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='passed_interview', to='jobboard.Candidate'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='interviewpassed',
            name='interview',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='passes', to='interview.ActionInterview'),
        ),
    ]
