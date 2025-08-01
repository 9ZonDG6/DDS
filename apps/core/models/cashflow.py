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
        ordering = ('id',)
        verbose_name = 'движение денежных средств'
        verbose_name_plural = 'движения денежных средств'

    def __str__(self) -> str:
        return f'{self.amount} ({self.created_at})'
