from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Post(models.Model):
    """Модель отдельной публикации"""
    text = models.TextField('Текст публикации',
                            help_text='Введите текст сообщения')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User,
        verbose_name='Автор публикации',
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Выберите автора публикации'
    )
    image = models.ImageField(
        verbose_name='Картинка для поста',
        upload_to='posts/',
        null=True,
        blank=True,
        help_text='Картинка для поста'
    )
    group = models.ForeignKey(
        'Group',
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='group_label',
        help_text='Выберите группу'
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.text[:15]


class Comment(models.Model):
    """Модель комментария к публикации"""
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

class Group(models.Model):
    """Модель сообщества"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title