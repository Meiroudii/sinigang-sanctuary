# Generated by Django 4.2.4 on 2024-04-09 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('dish', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=60)),
                ('content', models.TextField()),
                ('publish_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
