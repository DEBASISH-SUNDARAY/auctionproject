# Generated by Django 4.0.6 on 2022-07-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=30)),
                ('FirstName', models.CharField(max_length=30)),
                ('LastName', models.CharField(max_length=30)),
                ('MobileNo', models.CharField(max_length=15)),
                ('EmailId', models.CharField(max_length=50)),
                ('PassWord', models.CharField(max_length=30)),
            ],
        ),
    ]