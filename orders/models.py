from django.db import models
from django.db.models import F, Sum


class Order(models.Model):

    CHOICES = (
        ('N','New'),
        ('W','Waiting'),
        ('O','On the way'),
        ('M','Order_is_made'),
        ('R','Rejected')
    )

    customer = models.ForeignKey('user.Profiles', models.CASCADE, 'orders_cust', null=True, blank=True)
    courier = models.ForeignKey('user.Courier', models.CASCADE, 'orders_courier', null=True, blank=True)
    order_date = models.DateTimeField('Дата заказа', auto_now_add=True)
    address = models.CharField('Адресс', max_length=255)
    status = models.CharField('Статус', max_length=255, choices = CHOICES, default='N')
    total_price = models.DecimalField('Общая сумма', max_digits=10, decimal_places=2, null=True, blank=True, default=0)


    def get_total_price(self):
        return self.product_order.all().aggregate(total_price=Sum(F('quantity') * F('product__price')))['total_price']
        
        
    def save(self, *args, **kwargs):
        self.total_price = self.get_total_price()
        super(Order, self).save()
        print(2)

class OrderProduct(models.Model):
    quantity = models.PositiveIntegerField('Количество', default=1)
    product = models.ForeignKey('products.Product', models.CASCADE, 'orders')
    order = models.ForeignKey(Order, models.CASCADE, 'product_order')

    # почитатть про post save django 