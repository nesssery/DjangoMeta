# Generated by Django 2.2.7 on 2019-11-09 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0009_auto_20191109_1434'),
    ]

    operations = [
        migrations.AddField(
            model_name='metasmodels',
            name='video',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
