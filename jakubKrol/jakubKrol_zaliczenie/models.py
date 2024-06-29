from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=150, blank=False,
                             null=False, default='', unique=False)
    description = models.TextField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=120)
    year = models.PositiveSmallIntegerField(default=2024)
    image = models.ImageField(upload_to='media', blank=True, null=True)

    def __str__(self):
        return self.title_with_year()
    
    def title_with_year(self):
        return "{} ({})".format(self.title, self.year)

    class Meta:
        verbose_name = 'Artykuł'
        verbose_name_plural = 'Artykuły'
