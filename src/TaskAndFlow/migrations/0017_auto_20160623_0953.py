# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TaskAndFlow', '0016_flowtemplatestep_maxduration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectevent',
            name='relatetype',
            field=models.CharField(max_length=60, verbose_name=b'\xe5\x85\xb3\xe8\x81\x94\xe5\x85\x83\xe7\xb4\xa0\xe7\xb1\xbb\xe5\x9e\x8b', choices=[(b'\xe6\x9e\x84\xe4\xbb\xb6', b'\xe6\x9e\x84\xe4\xbb\xb6'), (b'\xe4\xbb\xbb\xe5\x8a\xa1', b'\xe4\xbb\xbb\xe5\x8a\xa1'), (b'\xe6\x96\xbd\xe5\xb7\xa5\xe6\x9c\xba\xe6\xa2\xb0', b'\xe6\x96\xbd\xe5\xb7\xa5\xe6\x9c\xba\xe6\xa2\xb0'), (b'\xe6\xb5\x81\xe7\xa8\x8b\xe6\xad\xa5\xe9\xaa\xa4', b'\xe6\xb5\x81\xe7\xa8\x8b\xe6\xad\xa5\xe9\xaa\xa4'), (b'\xe9\x87\x8d\xe5\xa4\xa7\xe5\x8d\xb1\xe9\x99\xa9\xe6\xba\x90\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95', b'\xe9\x87\x8d\xe5\xa4\xa7\xe5\x8d\xb1\xe9\x99\xa9\xe6\xba\x90\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95'), (b'\xe6\x96\xbd\xe5\xb7\xa5\xe6\x9c\xba\xe6\xa2\xb0\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95', b'\xe6\x96\xbd\xe5\xb7\xa5\xe6\x9c\xba\xe6\xa2\xb0\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95'), (b'\xe6\x9e\x84\xe4\xbb\xb6\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95', b'\xe6\x9e\x84\xe4\xbb\xb6\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95'), (b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95', b'\xe4\xbb\xbb\xe5\x8a\xa1\xe7\x8a\xb6\xe6\x80\x81\xe4\xbf\xae\xe6\x94\xb9\xe8\xae\xb0\xe5\xbd\x95')]),
            preserve_default=True,
        ),
    ]
