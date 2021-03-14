from django.db import models

# Create your models here.
class Tovar(models.Model):
    name = models.CharField(max_length=50, verbose_name = 'Наименование товара')
    cena = models.FloatField(verbose_name='Цена товара')
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT, verbose_name = 'Рубкика')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural='Товары'

    def __str__(self):
        return self.name

class Rubric(models.Model):
    name =models.CharField(max_length=50, db_index=True, verbose_name = 'Название рубрики')
    class Meta:
        verbose_name = 'Рубрика'
        verbose_name_plural='Рубрики'
        ordering = ['name']

    def __str__(self):
        return self.name
