# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=150)),
                ('short_body', models.TextField()),
                ('body', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('logo', models.ImageField(upload_to=b'static/')),
            ],
            options={
                'ordering': ('-timestamp',),
            },
        ),
    ]
