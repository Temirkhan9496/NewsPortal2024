from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Post, Category
from django.template.loader import render_to_string
from django.contrib.auth.models import User


@receiver(post_save, sender=Post)
def send_new_post_email(sender, instance, created, **kwargs):
    if created:
        category_subscribers = instance.category.subscribers.all()
        for subscriber in category_subscribers:
            subject = instance.title
            message = render_to_string('news/email_new_post.html', {
                'user': subscriber,
                'post': instance
            })
            send_mail(
                subject,
                message,
                'from@example.com',
                [subscriber.email],
                fail_silently=False,
            )


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = "Welcome to the NEWS_PORTAL"
        message = render_to_string('news/email_welcome.html', {
            'user': instance,
        })
        send_mail(
            subject,
            message,
            'from@example.com',
            [instance.email],
            fail_silently=False,
        )