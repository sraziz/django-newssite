# Generated by Django 3.0.5 on 2020-12-26 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(default=False, upload_to='imgs/'),
        ),
    ]
