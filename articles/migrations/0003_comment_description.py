# Generated by Django 4.1 on 2023-10-04 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_articles_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='description',
            field=models.TextField(default='No Comment', max_length=25),
        ),
    ]
