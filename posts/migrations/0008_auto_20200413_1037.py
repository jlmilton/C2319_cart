# Generated by Django 3.0.5 on 2020-04-13 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200412_0625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (4, 'Used - Not Usable'), (0, 'Brand New'), (1, 'Used - Like New'), (3, 'Used - Poor Condidtion')], default=4),
        ),
    ]
