# Generated by Django 2.2.6 on 2020-02-02 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20200202_0443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (2, 'Used - Good'), (4, 'Used - Not Working'), (3, 'Used - working'), (0, 'Brand New')], default=4),
        ),
    ]