# Generated by Django 3.1.3 on 2020-12-24 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20201120_1631'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=models.CharField(default='0000000000', max_length=10),
        ),
    ]
