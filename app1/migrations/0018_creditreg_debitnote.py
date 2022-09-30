# Generated by Django 4.0.4 on 2022-09-21 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0017_months_statistics_accounts_statistics_vouchers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='creditreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('particulars', models.CharField(max_length=255)),
                ('vouchertype', models.CharField(max_length=255)),
                ('voucherno', models.IntegerField()),
                ('debitamount', models.IntegerField(null=True)),
                ('creditamount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='debitnote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('particulars', models.CharField(max_length=255)),
                ('vouchertype', models.CharField(max_length=255)),
                ('voucherno', models.IntegerField()),
                ('debitamount', models.IntegerField()),
                ('creditamount', models.IntegerField(null=True)),
            ],
        ),
    ]
