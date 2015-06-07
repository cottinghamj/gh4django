# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('gittracker', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='filename',
            name='time_inserted',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 16, 21, 39, 6, 215171, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
