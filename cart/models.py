from django.db import models

from project.goods.models import Products
from project.users.models import User


class CartQueryset(models.QuerySet):
    def total_price(self):
        return sum(cart.products_price() for cart in self)

    def total_quantity(self):
        zero = 0
        if self:
            return sum(cart.quantity for cart in self)
        return zero


class Cart(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='������������')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='�����')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='����������')
    session_key = models.CharField(max_length=30, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='���� ����������')

    class Meta:
        db_table = 'cart'
        verbose_name = '�������'
        verbose_name_plural = '�������'

    objects = CartQueryset().as_manager()

    def products_price(self):
        return round(self.product.price * self.quantity, 2)

    def __str__(self):
        return f'������� {self.user.username} | ����� {self.product.name} | ���������� {self.quantity}'
