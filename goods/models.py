from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание товара')
    image = models.ImageField(
        upload_to='goods_images',
        blank=True,
        null=True,
        verbose_name='Изображение'
    )
    price = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Стоимость товара'
    )
    discount = models.DecimalField(
        default=0.00,
        max_digits=7,
        decimal_places=2,
        verbose_name='Скидка в %'
    )
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество товара')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'{self.name} Количество - {self.quantity}'

    def product_display(self):
        return f'{self.id:05}'


    # def price(self):

