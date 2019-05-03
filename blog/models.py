from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    status_normal = 1
    status_delete = 0
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
    )

    name = models.CharField(max_length=50, verbose_name="名称")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    is_nav = models.BooleanField(default=False, verbose_name="是否为导航")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "分类"

    def __str__(self):
        return self.name


class Tag(models.Model):
    status_normal = 1
    status_delete = 0
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
    )

    name = models.CharField(max_length=20, verbose_name="名称")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "标签"

    def __str__(self):
        return self.name


class Post(models.Model):
    status_normal = 1
    status_delete = 0
    status_draft = 2
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
        (status_draft, "草稿")
    )

    title = models.CharField(max_length=100, verbose_name="标题")
    desc = models.CharField(max_length=1024, blank=True, verbose_name="摘要")
    content = models.TextField(verbose_name="正文", help_text="正文必须为MarkDown格式")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="分类")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name="标签")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "文章"
        ordering = ["-id"] # 根据ID进行降序排列

    def __str__(self):
        return self.title