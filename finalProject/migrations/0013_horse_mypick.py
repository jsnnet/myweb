# Generated by Django 3.0.3 on 2020-02-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finalProject', '0012_auto_20200221_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Horse',
            fields=[
                ('answer_idx', models.AutoField(primary_key=True, serialize=False)),
                ('survey_idx', models.IntegerField()),
                ('num', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MyPick',
            fields=[
                ('survey_idx', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.TextField(null=True)),
                ('ans1', models.TextField(null=True)),
                ('ans2', models.TextField(null=True)),
                ('ans3', models.TextField(null=True)),
                ('ans4', models.TextField(null=True)),
                ('ans5', models.TextField(null=True)),
                ('ans6', models.TextField(null=True)),
                ('ans7', models.TextField(null=True)),
                ('ans8', models.TextField(null=True)),
                ('ans9', models.TextField(null=True)),
                ('ans10', models.TextField(null=True)),
                ('ans11', models.TextField(null=True)),
                ('ans12', models.TextField(null=True)),
                ('ans13', models.TextField(null=True)),
                ('ans14', models.TextField(null=True)),
                ('ans15', models.TextField(null=True)),
                ('ans16', models.TextField(null=True)),
                ('ans17', models.TextField(null=True)),
                ('ans18', models.TextField(null=True)),
                ('ans19', models.TextField(null=True)),
                ('ans20', models.TextField(null=True)),
                ('ans21', models.TextField(null=True)),
                ('ans22', models.TextField(null=True)),
                ('ans23', models.TextField(null=True)),
                ('ans24', models.TextField(null=True)),
                ('ans25', models.TextField(null=True)),
                ('ans26', models.TextField(null=True)),
                ('ans27', models.TextField(null=True)),
                ('ans28', models.TextField(null=True)),
                ('ans29', models.TextField(null=True)),
                ('ans30', models.TextField(null=True)),
                ('ans31', models.TextField(null=True)),
                ('ans32', models.TextField(null=True)),
                ('ans33', models.TextField(null=True)),
                ('ans34', models.TextField(null=True)),
                ('ans35', models.TextField(null=True)),
                ('ans36', models.TextField(null=True)),
                ('ans37', models.TextField(null=True)),
                ('ans38', models.TextField(null=True)),
                ('ans39', models.TextField(null=True)),
                ('ans40', models.TextField(null=True)),
                ('ans41', models.TextField(null=True)),
                ('ans42', models.TextField(null=True)),
                ('ans43', models.TextField(null=True)),
                ('ans44', models.TextField(null=True)),
                ('ans45', models.TextField(null=True)),
                ('ans46', models.TextField(null=True)),
                ('ans47', models.TextField(null=True)),
                ('ans48', models.TextField(null=True)),
                ('ans49', models.TextField(null=True)),
                ('ans50', models.TextField(null=True)),
                ('ans51', models.TextField(null=True)),
                ('ans52', models.TextField(null=True)),
                ('ans53', models.TextField(null=True)),
                ('ans54', models.TextField(null=True)),
                ('ans55', models.TextField(null=True)),
                ('ans56', models.TextField(null=True)),
                ('ans57', models.TextField(null=True)),
                ('ans58', models.TextField(null=True)),
                ('ans59', models.TextField(null=True)),
                ('ans60', models.TextField(null=True)),
                ('ans61', models.TextField(null=True)),
                ('status', models.CharField(default='y', max_length=1)),
            ],
        ),
    ]
