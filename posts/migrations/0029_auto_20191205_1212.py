# Generated by Django 2.2.7 on 2019-12-05 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0028_auto_20191204_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (4, 'Used - Not Working'), (1, 'Used - Like New'), (2, 'Used - Good'), (3, 'Used - working')], default=4),
        ),
    ]
