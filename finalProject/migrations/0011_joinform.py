# Generated by Django 3.0.3 on 2020-02-20 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('finalProject', '0010_delete_joinform'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinForm',
            fields=[
                ('mnum', models.AutoField(primary_key=True, serialize=False)),
                ('mid', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('mpwd', models.CharField(blank=True, max_length=50)),
                ('mname', models.CharField(blank=True, max_length=50)),
                ('mtel', models.IntegerField(blank=True, max_length=50)),
                ('madmin', models.CharField(choices=[('0', '회원'), ('1', '관리자')], max_length=10, null=True)),
                ('mdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
