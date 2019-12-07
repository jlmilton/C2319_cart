# Generated by Django 2.2.6 on 2019-12-02 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0018_auto_20191201_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Working'), (0, 'Brand New'), (2, 'Used - Good'), (1, 'Used - Like New'), (3, 'Used - working')], default=4),
        ),
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]