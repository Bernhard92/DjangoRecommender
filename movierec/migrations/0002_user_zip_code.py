# Generated by Django 2.2.1 on 2019-05-20 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movierec', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='zip_code',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
