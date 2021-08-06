# Generated by Django 3.1.3 on 2020-11-20 15:22

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='名稱')),
                ('sub_title', models.CharField(default='', max_length=200, verbose_name='副標題')),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('image', models.ImageField(blank=True, upload_to='category/%Y/%m/%d/', verbose_name='圖片')),
            ],
            options={
                'verbose_name': '產品分類',
                'verbose_name_plural': '產品分類',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Page_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='No Setting', max_length=100, unique=True, verbose_name='項目')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='內容')),
            ],
            options={
                'verbose_name': '網站內容',
                'verbose_name_plural': '網站內容',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d')),
                ('overview', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='商品特色')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='詳細資訊')),
                ('specifications', ckeditor.fields.RichTextField(blank=True, verbose_name='商品規格')),
                ('price', models.DecimalField(decimal_places=0, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('available', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='shop.category')),
            ],
            options={
                'verbose_name_plural': '產品',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]