# Generated by Django 2.2.6 on 2019-10-18 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=40)),
                ('for_men', models.BooleanField()),
                ('category', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=5)),
                ('shoe_size', models.IntegerField()),
                ('price', models.FloatField()),
                ('images', models.ImageField(upload_to='')),
                ('lot', models.IntegerField()),
            ],
        ),
    ]
