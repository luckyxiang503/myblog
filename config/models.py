from django.db import models
from blog.models import User
from django.template.loader import render_to_string

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
    display_html = 1
    display_latest = 2
    display_hot = 3
    display_comment = 4
    side_type = (
        (display_html, "HTML"),
        (display_latest, "最新文章"),
        (display_hot, "最热文章"),
        (display_comment, "最新评论")
    )

    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=side_type, verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容", help_text="如果设置的不是HTML类型,可为空")
    status = models.PositiveIntegerField(default=status_normal, choices=status_items, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"

    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.status_normal)

    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment

        result = ''
        if self.display_type == self.display_html:
            result = self.content
        elif self.display_type == self.display_latest:
            context = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/sidebar_post.html', context=context)
        elif self.display_type == self.display_hot:
            context = {
                'posts': Post.hot_posts()
            }
            result = render_to_string('config/sidebar_post.html', context=context)
        elif self.display_type == self.display_comment:
            context = {
                'comments': Comment.objects.filter(status=Comment.status_normal).select_related('target')
            }
            result = render_to_string('config/sidebar_comment.html', context=context)
        return result