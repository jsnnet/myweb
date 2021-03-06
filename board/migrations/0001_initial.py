# Generated by Django 3.0.2 on 2020-01-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BBS_comm',
            fields=[
                ('number_idx', models.AutoField(primary_key=True, serialize=False)),
                ('tcode', models.IntegerField()),
                ('comm', models.TextField(null=True)),
                ('writer', models.TextField(null=True)),
                ('pwd', models.TextField(null=True)),
                ('no_idx', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Board',
            fields=[
                ('no_idx', models.AutoField(primary_key=True, serialize=False)),
                ('pwd', models.TextField(null=True)),
                ('writer', models.TextField(null=True)),
                ('subject', models.TextField(null=True)),
                ('content', models.TextField(null=True)),
                ('regdate', models.TextField(null=True)),
            ],
        ),
    ]
