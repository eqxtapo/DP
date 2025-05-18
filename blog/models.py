from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок блога")
    # slug = slugify("Пример блога")
    description = models.TextField(null=True)
    image = models.ImageField(
        upload_to="images/", blank=True, null=True, verbose_name="Изображение"
    )
    created_at = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False, verbose_name="Уже тут")
    views_counter = models.PositiveIntegerField(
        verbose_name="Количество просмотров", default=0
    )

    def __str__(self):
        return f"{self.title} "

    class Meta:
        verbose_name = "блог"
        verbose_name_plural = "блоги"