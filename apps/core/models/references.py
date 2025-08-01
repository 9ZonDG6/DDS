from django.db import models


class Status(models.Model):
    name = models.CharField('название статуса', max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def __str__(self) -> str:
        return self.name


class FlowType(models.Model):
    name = models.CharField('название типа', max_length=255)

    class Meta:
        ordering = ('id',)
        verbose_name = 'тип'
        verbose_name_plural = 'типы'

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField('название категории', max_length=255)
    flow_type = models.ForeignKey('FlowType', verbose_name='тип', related_name='categories', on_delete=models.CASCADE)

    class Meta:
        ordering = ('id',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        constraints = [models.UniqueConstraint(fields=['flow_type', 'name'], name='uniq_category_per_flow_type')]

    def __str__(self) -> str:
        return self.name


class SubCategory(models.Model):
    name = models.CharField('название подкатегории', max_length=255)
    category = models.ForeignKey(
        'Category', verbose_name='категория', related_name='subcategories', on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        constraints = [models.UniqueConstraint(fields=['category', 'name'], name='uniq_subcategory_per_category')]

    def __str__(self) -> str:
        return self.name
