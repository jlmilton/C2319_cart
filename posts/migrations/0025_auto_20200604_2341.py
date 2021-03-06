# Generated by Django 3.0.5 on 2020-06-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0024_auto_20200427_1927'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='item_label',
            field=models.CharField(choices=[(0, 'Best-Seller'), (1, 'Must Have'), (2, 'durable'), (3, 'Best Bang for your buck'), (4, 'Pollitzer Award')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (0, 'Brand New'), (1, 'Used - Like New'), (2, 'Used - Good')], default=4),
        ),
    ]
