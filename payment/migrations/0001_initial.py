# Generated by Django 3.1.3 on 2020-12-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ecpay_Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MerchantID', models.CharField(max_length=30, verbose_name='特店編號')),
                ('MerchantTradeNo', models.CharField(max_length=30, verbose_name='特店交易編號')),
                ('RtnCode', models.IntegerField(verbose_name='交易狀態')),
                ('TradeNo', models.CharField(max_length=30, verbose_name='綠界交易編號')),
                ('TradeAmt', models.IntegerField(verbose_name='交易金額')),
                ('PaymentDate', models.DateTimeField()),
            ],
            options={
                'verbose_name': '綠界訂單',
                'verbose_name_plural': '綠界訂單',
            },
        ),
    ]
