# Generated by Django 4.2.3 on 2023-07-24 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annotations', '0048_auto_20220103_1610'),
    ]

    operations = [
        migrations.AddField(
            model_name='annotationtype',
            name='multi_frame',
            field=models.BooleanField(default=False),
        ),
    ]
