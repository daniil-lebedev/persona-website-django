# Generated by Django 3.2.2 on 2021-05-09 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogs',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
