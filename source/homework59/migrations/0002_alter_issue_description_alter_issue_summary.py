# Generated by Django 4.1.7 on 2023-03-09 15:26

from django.db import migrations, models
import homework59.models.issue


class Migration(migrations.Migration):

    dependencies = [
        ('homework59', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='description',
            field=models.TextField(max_length=254, null=True, validators=[homework59.models.issue.validate_description_no_bad_words], verbose_name='Полное описание'),
        ),
        migrations.AlterField(
            model_name='issue',
            name='summary',
            field=models.CharField(max_length=100, validators=[homework59.models.issue.validate_summary_no_digits, homework59.models.issue.validate_summary_capitalized], verbose_name='Краткое описание'),
        ),
    ]
