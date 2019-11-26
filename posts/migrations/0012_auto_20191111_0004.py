# Generated by Django 2.2.6 on 2019-11-11 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_post_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.IntegerField(choices=[(0, 'Electronic'), (1, 'Furniture'), (2, 'Major Appliance'), (3, 'Kitchen'), (4, 'Books'), (5, 'Motors')], default=0),
        ),
    ]