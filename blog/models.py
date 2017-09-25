from django.db import models
from django.contrib.auth.models import User
from gafferon_games.settings import BASE_DIR
import os


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=300, unique=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=300, unique=True)
    subtitle = models.CharField(max_length=300)
    content_filename = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='articles')
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-created', ]

    def __str__(self):
        return 'Article {0} from category {1}'.format(self.title, self.category.title)

    @property
    def formatted_date(self):
        return self.created.date().strftime('%A, %B %d, %Y')

    @property
    def content(self):
        filename = os.path.join(BASE_DIR, 'articles/' + self.content_filename)
        try:
            with open(filename, 'r') as file:
                content = file.readlines()
                content = ''.join(content)
        except IOError:
            content = '<h1>Error while content loading</h1>'
        return content

    def save(self, *args, **kwargs):
        content = self.content_filename
        filename = '{0}_{1}'.format(self.category_id,
                                    Article.objects.latest('id').id if Article.objects.exists() else 1) + '.html'
        self.content_filename = filename
        filename = os.path.join(BASE_DIR, 'articles/' + filename)
        with open(filename, 'w') as file:
            file.write(content)
        super(Article, self).save(*args, **kwargs)
