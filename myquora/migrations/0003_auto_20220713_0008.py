# Generated by Django 3.2.9 on 2022-07-12 18:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myquora', '0002_alter_answer_date_created_alter_answer_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 477001, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 477001, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='author',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 473989, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 475005, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 476003, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_created',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 479000, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='date_updated',
            field=models.DateField(default=datetime.datetime(2022, 7, 12, 18, 38, 25, 479000, tzinfo=utc), null=True),
        ),
    ]
