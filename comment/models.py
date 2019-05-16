from django.db import models
from blog.models import Post


class Comment(models.Model):
    status_normal = 1
    status_delete = 0
    status_items = (
        (status_normal, "正常"),
        (status_delete, "删除"),
    )

    target = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name="评论目标")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="呢称")
    website = models.URLField(verbose_name="网页")
    email = models.EmailField(verbose_name="邮箱")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
