# Generated by Django 3.0 on 2020-03-30 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0030_auto_20200329_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (1, 'Used - Like New'), (0, 'Brand New')], default=4),
        ),
    ]
