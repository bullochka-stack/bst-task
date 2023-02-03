from django.conf import settings
from django.core.mail import send_mail


def send_email(customer, robot):
    """
    Функция отправляет сообщение на электронную почту пользователя.
    :param customer:
    :param robot:
    :return:
    """
    subject = 'Появился новый робот по вашему запросу'
    html_content = 'Добрый день!\n'
    html_content += f'Недавно вы интересовались нашим роботом модели {robot.model}, версии {robot.version}.\nЭтот ' \
                    f'робот теперь в наличии. Если вам подходит этот вариант - пожалуйста, свяжитесь с нами.'
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject=subject, message=html_content, from_email=email_from, recipient_list=[customer.email],)
