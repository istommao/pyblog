"""app models."""
from django.db import models

from simditor.fields import RichTextField

from extension.modelutils import RandomFixedCharField, PathAndRename

from app import consts


class Column(models.Model):
    """Column Model."""
    uid = RandomFixedCharField('编号', max_length=8, unique=True)
    image = models.ImageField(
        '图片', upload_to=PathAndRename('info/'),
        default=consts.DEFAULT_IMAGE
    )

    name = models.CharField('名称', max_length=32)
    intro = models.CharField('简介', max_length=128, default='')
    content = RichTextField(verbose_name='内容', default='')

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        """Column Meta."""
        verbose_name = '专栏管理'
        verbose_name_plural = '专栏管理'


class Article(models.Model):
    """Article Model."""

    uid = RandomFixedCharField('编号', max_length=16, unique=True)
    image = models.ImageField(
        '图片', upload_to=PathAndRename('info/'),
        default=consts.DEFAULT_IMAGE
    )

    title = models.CharField('标题', max_length=32)
    intro = models.CharField('简介', max_length=128, default='')
    content = RichTextField(verbose_name='内容', default='')

    creation_time = models.DateTimeField('创建时间', auto_now_add=True)

    column = models.ForeignKey('app.Column', verbose_name='专栏',
                               related_name='articles',
                               null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        """Article Meta."""
        verbose_name = '文章管理'
        verbose_name_plural = '文章管理'


# class News(models.Model):
#     """News model."""

#     uid = RandomFixedCharField('编号', max_length=16, unique=True)
#     image = models.ImageField(
#         '图片', upload_to=PathAndRename('news/'),
#         default=consts.DEFAULT_IMAGE
#     )

#     title = models.CharField('标题', max_length=32)
#     intro = models.CharField('简介', max_length=128, default='')
#     link = models.URLField('链接')

#     creation_time = models.DateTimeField('创建时间', auto_now_add=True)

#     def __str__(self):
#         return self.title

#     class Meta:
#         """Article Meta."""
#         verbose_name = '新闻管理'
#         verbose_name_plural = '新闻管理'
