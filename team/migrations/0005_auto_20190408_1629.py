# Generated by Django 2.1.7 on 2019-04-08 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0004_auto_20190408_1621'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='request',
            unique_together=set(),
        ),
    ]