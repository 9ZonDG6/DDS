from datetime import date

from django.db import models


class CashFlow(models.Model):
    amount = models.DecimalField('кол-во средств в рублях', max_digits=14, decimal_places=2)
    status = models.ForeignKey(
        'Status',
        verbose_name='статус',
        related_name='cashflows',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    flow_type = models.ForeignKey('FlowType', verbose_name='тип', related_name='cashflows', on_delete=models.PROTECT)
    category = models.ForeignKey(
        'Category', verbose_name='категория', related_name='cashflows', on_delete=models.PROTECT
    )
    subcategory = models.ForeignKey(
        'SubCategory', verbose_name='подкатегория', related_name='cashflows', on_delete=models.PROTECT
    )
    comment = models.TextField('комментарий', null=True, blank=True, help_text='комментарий к записи в свободной форме')
    created_at = models.DateField('дата создания', default=date.today)

    class Meta:
        verbose_name = 'движение денежных средств'
        verbose_name_plural = 'движения денежных средств'

    def __str__(self) -> str:
        return f'{self.amount} ({self.created_at})'


class Status(models.Model):
    name = models.CharField('название статуса', max_length=255)

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'

    def __str__(self) -> str:
        return self.name


class FlowType(models.Model):
    name = models.CharField('название типа', max_length=255)

    class Meta:
        verbose_name = 'тип'
        verbose_name_plural = 'типы'

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField('название категории', max_length=255)
    flow_type = models.ForeignKey('FlowType', verbose_name='тип', related_name='categories', on_delete=models.CASCADE)

    class Meta:
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
        verbose_name = 'подкатегория'
        verbose_name_plural = 'подкатегории'
        constraints = [models.UniqueConstraint(fields=['category', 'name'], name='uniq_subcategory_per_category')]

    def __str__(self) -> str:
        return self.name
