# Generated by Django 2.0.3 on 2018-04-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clicker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='alcochol',
            field=models.IntegerField(default=0, verbose_name='alcochol'),
        ),
        migrations.AddField(
            model_name='event',
            name='cigaretes',
            field=models.IntegerField(default=0, verbose_name='cigaretes'),
        ),
        migrations.AddField(
            model_name='event',
            name='drugs',
            field=models.IntegerField(default=0, verbose_name='drugs'),
        ),
        migrations.AddField(
            model_name='event',
            name='friends',
            field=models.IntegerField(default=0, verbose_name='friends'),
        ),
        migrations.AddField(
            model_name='event',
            name='stress',
            field=models.IntegerField(default=0, verbose_name='stress'),
        ),
    ]
