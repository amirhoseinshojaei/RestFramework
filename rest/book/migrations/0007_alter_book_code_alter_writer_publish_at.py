# Generated by Django 5.0.1 on 2024-01-27 05:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_alter_book_code_alter_writer_publish_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='code',
            field=models.CharField(default='jB3AOJ2ejJfW9vNSgH3CT8msvaAp64Gjy5EPw00dx6lKGRfj0I', max_length=50),
        ),
        migrations.AlterField(
            model_name='writer',
            name='publish_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 27, 5, 19, 29, 603325, tzinfo=datetime.timezone.utc)),
        ),
    ]
