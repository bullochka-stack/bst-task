from django.db.models.signals import post_save
from django.dispatch import receiver
from robots.models import Robot
from .models import Order
from .services import send_email


@receiver(post_save, sender=Robot)
def check_robot_serial(sender, instance, created, **kwargs):
    """
    Функция-сигнал. Если робот создан, проверяет есть ли заказ на этого робота.
    Если есть - вызывает функцию отправки письма.
    :param sender:
    :param instance:
    :param created:
    :param kwargs:
    :return:
    """
    if created:
        orders = Order.objects.filter(robot_serial=instance.serial)
        if orders.exists():
            first_order = orders[0]
            customer = first_order.customer
            send_email(customer=customer, robot=instance)
