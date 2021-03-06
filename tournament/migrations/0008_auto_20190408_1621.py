# Generated by Django 2.1.7 on 2019-04-08 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20190408_1621'),
        ('tournament', '0007_auto_20190317_1635'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='enrollment',
            unique_together={('tournament', 'team')},
        ),
        migrations.AlterUniqueTogether(
            name='invite',
            unique_together={('tournament', 'team')},
        ),
    ]
