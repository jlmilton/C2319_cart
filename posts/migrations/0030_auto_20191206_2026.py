# Generated by Django 2.2.5 on 2019-12-07 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0029_auto_20191205_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - working'), (0, 'Brand New'), (4, 'Used - Not Working'), (2, 'Used - Good'), (1, 'Used - Like New')], default=4),
        ),
    ]
