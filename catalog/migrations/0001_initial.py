# Generated by Django 4.2.7 on 2024-01-14 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=40)),
                ('message_category', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('message', models.TextField()),
                ('photo', models.ImageField(upload_to='static/')),
                ('name_category', models.CharField(max_length=40)),
                ('unit_price', models.IntegerField()),
                ('date_of_creation', models.DateTimeField()),
                ('last_modified_date', models.DateTimeField()),
            ],
        ),
    ]