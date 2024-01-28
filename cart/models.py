# from django.db import models
#
# from project.goods.models import Products
# from project.users.models import User
#
#
# class Cart(models.Model):
#     product = models.ForeignKey(to=Products, on_delete=models.CASCADE)
#     user = models.ForeignKey(to=User, on_delete=models.CASCADE)
#     time_add = models.TimeField()
#
#     class Meta:
#         db_table = 'cart'
#         verbose_name = 'Корзину'
#         verbose_name_plural = 'Корзины'
#
#
#
