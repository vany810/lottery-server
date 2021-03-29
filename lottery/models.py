from django.db import models
from django.conf import settings
import logging

logger = logging.getLogger('django')


class LotteryActivity(models.Model):
    name = models.CharField('活动名称', max_length=150)
    date = models.DateField('举办日期')

    class Meta:
        ordering = ['-date']
        verbose_name = '抽奖活动'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Prize(models.Model):
    activity = models.ForeignKey(LotteryActivity, on_delete=models.CASCADE, verbose_name='活动')
    name = models.CharField('奖品名称', max_length=120)
    count = models.PositiveSmallIntegerField('奖品数量')
    award = models.CharField('奖项', max_length=20)
    order = models.PositiveIntegerField('排序值', unique=True, null=True, blank=True,
                                        help_text='数值大的奖品排序在前，默认值与id相同')
    image = models.ImageField('图片', upload_to='prize_images')

    class Meta:
        ordering = ['order']
        verbose_name = '奖品'
        verbose_name_plural = verbose_name

    def save(self, *args, **kwargs):
        logger.info('奖品id为：{}'.format(self.id))
        super().save(*args, **kwargs)
        if not self.order:
            self.order = self.id
            self.save()

    def __str__(self):
        return '{} {}'.format(self.award, self.name)


class LotteryRecord(models.Model):
    activity = models.ForeignKey(LotteryActivity, on_delete=models.CASCADE, verbose_name='活动')
    prize = models.ForeignKey(Prize, on_delete=models.CASCADE, verbose_name='奖品')
    created_at = models.DateTimeField('创建时间', auto_now_add=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='用户',
        help_text='中奖人员'
    )

    class Meta:
        ordering = ['created_at']
        verbose_name = '中奖记录'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} - {}'.format(self.user, self.prize)


class LotteryUser(models.Model):
    activity = models.ForeignKey(LotteryActivity, on_delete=models.CASCADE, verbose_name='活动')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='用户'
    )

    class Meta:
        verbose_name = '抽奖名单'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{} - {}'.format(self.activity, self.user)
