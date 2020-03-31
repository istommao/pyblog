# Generated by Django 2.1 on 2020-03-31 22:53

from django.db import migrations, models
import django.db.models.deletion
import extension.modelutils
import simditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', extension.modelutils.RandomFixedCharField(editable=False, max_length=16, unique=True, verbose_name='编号')),
                ('image', models.ImageField(default='app/default.png', upload_to=extension.modelutils.PathAndRename('info/'), verbose_name='图片')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('intro', models.CharField(default='', max_length=128, verbose_name='简介')),
                ('content', simditor.fields.RichTextField(default='', verbose_name='内容')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '文章管理',
                'verbose_name_plural': '文章管理',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', extension.modelutils.RandomFixedCharField(editable=False, max_length=8, unique=True, verbose_name='编号')),
                ('image', models.ImageField(default='app/default.png', upload_to=extension.modelutils.PathAndRename('info/'), verbose_name='图片')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('intro', models.CharField(default='', max_length=128, verbose_name='简介')),
                ('content', simditor.fields.RichTextField(default='', verbose_name='内容')),
                ('creation_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '专栏管理',
                'verbose_name_plural': '专栏管理',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='column',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='articles', to='app.Column', verbose_name='专栏'),
        ),
    ]