# Generated by Django 3.1.7 on 2021-03-29 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='活动名称')),
                ('date', models.DateField(verbose_name='举办日期')),
            ],
            options={
                'verbose_name': '抽奖活动',
                'verbose_name_plural': '抽奖活动',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='LotteryRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '中奖记录',
                'verbose_name_plural': '中奖记录',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Prize',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='奖品名称')),
                ('count', models.PositiveSmallIntegerField(verbose_name='奖品数量')),
                ('award', models.CharField(max_length=20, verbose_name='奖项')),
                ('order', models.PositiveIntegerField(blank=True, help_text='数值大的奖品排序在前，默认值与id相同', null=True, unique=True, verbose_name='排序值')),
                ('image', models.ImageField(upload_to='prize_images', verbose_name='图片')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.lotteryactivity', verbose_name='活动')),
            ],
            options={
                'verbose_name': '奖品',
                'verbose_name_plural': '奖品',
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='LotteryUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lottery.lotteryactivity', verbose_name='活动')),
            ],
            options={
                'verbose_name': '抽奖名单',
                'verbose_name_plural': '抽奖名单',
            },
        ),
    ]
