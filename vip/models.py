from django.db import models

class VIP_User(models.Model):
    name = models.CharField(max_length=10, verbose_name='名稱', default='')
    line_id = models.CharField(max_length=60, verbose_name='line_id', default='')
    actived = models.BooleanField(verbose_name='啟用', default=False)

    class Meta:
        ordering = ('name',)
        verbose_name = '會員'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
