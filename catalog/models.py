from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=40)
    message_category = models.TextField()

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    name = models.CharField(max_length=40)
    message = models.TextField()
    photo = models.ImageField(upload_to='product_photos/')
    name_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_price = models.IntegerField()
    date_of_creation = models.DateTimeField(auto_now_add=True)
    last_modified_date = models.DateTimeField(auto_now=True)
    #created_at=models.TextField(default='none' )

    def __str__(self):
        return f'{self.title} {self.category}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'