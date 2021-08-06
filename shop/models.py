from django.urls import reverse
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField, RichTextUploadingFormField

class Page_Content(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="項目", default="請設定")
    content = RichTextUploadingField(blank=True, verbose_name="內容")
    slug = models.CharField(max_length=100, verbose_name='slug', default='請設定')

    class Meta:
        verbose_name = '網站內容'
        verbose_name_plural = verbose_name

class Category(models.Model):
    name = models.CharField(max_length=200,
                            db_index=True, verbose_name='名稱')
    sub_title = models.CharField(max_length=200, default='', verbose_name='副標題')
    slug = models.SlugField(max_length=200,
                            db_index=True,
                            unique=True)
    image = models.ImageField(upload_to='category/%Y/%m/%d/', blank=True, verbose_name='圖片')

    class Meta:
        ordering = ('name',)
        verbose_name = '產品分類'
        verbose_name_plural = '產品分類'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d',
                              blank=True)
    overview = RichTextUploadingField(blank=True, verbose_name="商品特色")
    description = RichTextUploadingField(blank=True, verbose_name="詳細資訊")
    specifications = RichTextField(blank=True, verbose_name="商品規格")
    # 台灣價錢都是整數，所以可以設定 decimal_places=0
    price = models.DecimalField(max_digits=10, decimal_places=0)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = '產品'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
