# Generated by Django 2.2.7 on 2019-11-07 13:50

from django.db import migrations, models
import meta.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelsMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            bases=(meta.models.ModelMeta, models.Model),
        ),
    ]
