# Generated by Django 4.2.5 on 2023-09-15 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_alter_post_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
