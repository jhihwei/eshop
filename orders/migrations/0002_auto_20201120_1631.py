# Generated by Django 3.1.3 on 2020-11-20 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ('-created',), 'verbose_name': '訂單', 'verbose_name_plural': '訂單'},
        ),
    ]