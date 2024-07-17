# настройка отправки писем при различных действиях пользователя

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from .models import Article, Subscription
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Добро пожаловать на наш новостной портал!'
        message = f'Здравствуйте, {instance.username}! Спасибо за регистрацию на нашем сайте.'
        send_mail(subject, message, 'from@example.com', [instance.email])

@receiver(post_save, sender=Article)
def send_article_notification(sender, instance, created, **kwargs):
    if created:
        subscriptions = Subscription.objects.filter(category=instance.category)
        for subscription in subscriptions:
            user = subscription.user
            subject = f'Новая статья в категории {instance.category.name}'
            html_message = render_to_string('news/article_email.html', {'article': instance})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'from@example.com', [user.email])

@receiver(post_save, sender=Subscription)
def send_subscription_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = f'Вы подписались на категорию {instance.category.name}'
        message = f'Здравствуйте, {instance.user.username}! Вы подписались на категорию {instance.category.name}.'
        send_mail(subject, message, 'from@example.com', [instance.user.email])