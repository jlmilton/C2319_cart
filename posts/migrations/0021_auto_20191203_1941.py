# Generated by Django 2.2.6 on 2019-12-04 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_auto_20191203_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (2, 'Used - Good'), (3, 'Used - working'), (0, 'Brand New'), (4, 'Used - Not Working')], default=4),
        ),
    ]