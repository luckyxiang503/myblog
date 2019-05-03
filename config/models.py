from django.db import models
from blog.models import User


class Link(models.Model):
    status_normal = 1
    status_delete = 0
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
    )

    title = models.CharField(max_length=100, verbose_name="标题")
    href = models.URLField(verbose_name="链接") # 默认长度为200
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    weight = models.PositiveIntegerField(default=1, choices=zip(range(1, 6), range(1, 6)),
                                         verbose_name="权重",
                                         help_text="权重高展示顺序靠前")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "友链"


class SideBar(models.Model):
    status_normal = 1
    status_delete = 0
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
    )
    side_type = (
        (1, "HTML"),
        (2, "最新文章"),
        (3, "最热文章"),
        (4, "最新评论")
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=side_type, verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容", help_text="如果设置的不是HTML类型,可为空")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"