# Generated by Django 3.0.3 on 2020-03-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0019_auto_20200301_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (4, 'Used - Not Working'), (3, 'Used - working'), (2, 'Used - Good'), (1, 'Used - Like New')], default=4),
        ),
    ]
