# Generated by Django 3.0.7 on 2020-06-25 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='corona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.IntegerField()),
                ('affected', models.IntegerField()),
                ('recovared', models.IntegerField()),
                ('deth', models.IntegerField()),
                ('total_test', models.IntegerField()),
                ('total_affected', models.IntegerField()),
                ('totel_recovared', models.IntegerField()),
                ('total_deth', models.IntegerField()),
            ],
        ),
    ]
