# Generated by Django 2.2 on 2024-09-03 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='site',
            field=models.CharField(default='http://default.example.com', max_length=255),
            preserve_default=False,
        ),
    ]
