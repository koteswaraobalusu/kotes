# Generated by Django 5.0.3 on 2024-03-08 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_likepost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likepost',
            name='post_id',
            field=models.CharField(max_length=1000),
        ),
    ]