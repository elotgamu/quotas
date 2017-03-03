# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-07 04:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('printers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'material_type',
                'verbose_name_plural': 'material_types',
            },
        ),
        migrations.CreateModel(
            name='Quota',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('before_date', models.DateTimeField()),
                ('is_active', models.BooleanField(default=True)),
                ('responses_number', models.IntegerField(default=0)),
                ('quota_type', models.CharField(choices=[('Digital', 'Offset'), ('Offset', 'Digital')], max_length=50)),
                ('size', models.CharField(max_length=50)),
                ('quiebres', models.IntegerField()),
                ('single_side', models.BooleanField(default=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.Customer')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.Material')),
            ],
            options={
                'verbose_name': 'Quota',
                'verbose_name_plural': 'Quotas',
            },
        ),
        migrations.CreateModel(
            name='quota_response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.FloatField()),
                ('deliver_time', models.DateTimeField()),
                ('extra_details', models.TextField()),
                ('has_prepayment', models.BooleanField(default=True)),
                ('prepayment_amount', models.DecimalField(decimal_places=2, max_digits=4)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('offered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printers.Printer')),
                ('quota', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotation.Quota')),
            ],
            options={
                'verbose_name': 'quota_response',
                'verbose_name_plural': 'quota_responses',
            },
        ),
    ]
