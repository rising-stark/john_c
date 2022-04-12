# Generated by Django 4.0.4 on 2022-04-12 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=100)),
                ('company_benefits_detail', models.TextField(blank=True, null=True)),
                ('company_bonus_detail', models.TextField(blank=True, null=True)),
                ('company_equity_detail', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Recipient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('recipient_firstname', models.CharField(max_length=100)),
                ('recipient_lastname', models.CharField(max_length=100)),
                ('recipient_salary', models.IntegerField(blank=True, default=0, null=True)),
                ('recipient_bonus', models.IntegerField(blank=True, default=0, null=True)),
                ('recipient_equity', models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
    ]
