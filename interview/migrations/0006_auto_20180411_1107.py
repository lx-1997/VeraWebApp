# Generated by Django 2.0.3 on 2018-04-11 11:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0005_interview_closed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actioninterview',
            name='interview',
        ),
        migrations.AddField(
            model_name='interview',
            name='action_interview',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='interviews', to='interview.ActionInterview'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='actioninterview',
            name='interviewer',
            field=models.CharField(choices=[('me', 'Me'), ('vera', 'Vera')], max_length=64),
        ),
    ]