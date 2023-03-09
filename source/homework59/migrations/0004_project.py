# Generated by Django 4.1.7 on 2023-03-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework59', '0003_issue_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(null=True, verbose_name='Дата окончания')),
                ('name', models.CharField(max_length=50, verbose_name='Название')),
                ('description', models.TextField(max_length=254, null=True, verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Проект',
                'verbose_name_plural': 'Проекты',
            },
        ),
    ]