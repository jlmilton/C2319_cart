# Generated by Django 3.0.5 on 2020-06-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0025_auto_20200604_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (0, 'Brand New'), (4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (1, 'Used - Like New')], default=4),
        ),
    ]
