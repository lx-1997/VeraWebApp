# Generated by Django 2.0.3 on 2018-03-23 11:24

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jobboard', '0001_initial'),
        ('vacancy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name="Answer's text")),
                ('weight', models.SmallIntegerField(default=1, help_text='Value from -100 to 100')),
            ],
            options={
                'ordering': ('?',),
            },
        ),
        migrations.CreateModel(
            name='AnswerForVerification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('processed', models.BooleanField(default=False)),
                ('points', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('employer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='jobboard.Employer')),
                ('parent_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sub_categories', to='quiz.Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='ExamPassing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answers', jsonfield.fields.JSONField()),
                ('points', models.IntegerField(default=0)),
                ('processed', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('candidate', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exams', to='jobboard.Candidate')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name="Question's text")),
                ('weight', models.SmallIntegerField(default=1, help_text='Value from -100 to 100')),
                ('is_published', models.BooleanField(default=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='quiz.Category')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('template_name', models.CharField(help_text='*_question.html', max_length=25)),
                ('w2v', models.BooleanField(default=False)),
                ('min_answers', models.PositiveSmallIntegerField(default=0)),
                ('one_right_answer', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='VacancyExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('max_attempts', models.PositiveIntegerField(default=3)),
                ('passing_grade', models.PositiveIntegerField(default=0)),
                ('max_points', models.PositiveIntegerField(default=0)),
                ('questions', models.ManyToManyField(to='quiz.Question')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='vacancy.Vacancy')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='kind',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='quiz.QuestionKind'),
        ),
        migrations.AddField(
            model_name='exampassing',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.VacancyExam'),
        ),
        migrations.AddField(
            model_name='answerforverification',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='verifications', to='quiz.Question'),
        ),
        migrations.AddField(
            model_name='answerforverification',
            name='related_answer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='quiz.Answer'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='quiz.Question'),
        ),
    ]