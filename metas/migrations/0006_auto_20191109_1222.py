# Generated by Django 2.2.7 on 2019-11-09 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0005_othermeta'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OtherMeta',
        ),
        migrations.RenameField(
            model_name='metamodel',
            old_name='nom',
            new_name='title',
        ),
    ]
