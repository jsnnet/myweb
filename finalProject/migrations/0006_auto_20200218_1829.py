# Generated by Django 3.0.3 on 2020-02-18 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalProject', '0005_auto_20200217_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignupForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mid', models.CharField(blank=True, max_length=50)),
                ('mpwd', models.CharField(blank=True, max_length=50)),
                ('mname', models.DateField(blank=True, null=True)),
                ('mtel', models.CharField(blank=True, max_length=50)),
                ('madmin', models.IntegerField(max_length=1)),
                ('mdate', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='DjangoBoard',
        ),
    ]
