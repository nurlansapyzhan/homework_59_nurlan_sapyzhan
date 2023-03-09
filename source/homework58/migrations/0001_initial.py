# Generated by Django 4.1.7 on 2023-03-06 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=100, verbose_name='Краткое описание')),
                ('description', models.TextField(max_length=254, null=True, verbose_name='Полное описание')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Дата и время обновления')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Статус задачи')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Тип задачи')),
            ],
            options={
                'verbose_name': 'Тип задачи',
                'verbose_name_plural': 'Типы задач',
            },
        ),
        migrations.CreateModel(
            name='IssueType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='issue_types', to='homework58.issue', verbose_name='Задача')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_issues', to='homework58.type', verbose_name='Тип')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homework58.status'),
        ),
        migrations.AddField(
            model_name='issue',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='issues', through='homework58.IssueType', to='homework58.type'),
        ),
    ]
