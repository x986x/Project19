# Generated by Django 4.2.6 on 2024-03-07 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('slug', models.CharField(blank=True, max_length=150, null=True, verbose_name='slug')),
                ('body', models.TextField(verbose_name='Содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение')),
                ('date_of_creation', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='Просмотры')),
            ],
            options={
                'verbose_name': 'блоговая запись',
                'verbose_name_plural': 'блоговые записи',
            },
        ),
    ]
