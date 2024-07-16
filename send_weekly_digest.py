from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from datetime import timedelta
from news.models import Post, Category


class Command(BaseCommand):
    help = 'Send weekly digest to subscribers'

    def handle(self, *args, **kwargs):
        last_week = timezone.now() - timedelta(days=7)
        categories = Category.objects.all()
        for category in categories:
            posts = Post.objects.filter(categories=category, created_at__gte=last_week)
            if posts.exists():
                subscribers = set(user.email for user in category.subscribers.all())
                subject = f'Еженедельная рассылка новостей по категории {category.name}'
                message = render_to_string('email/weekly_digest.html', {'posts': posts, 'category': category})
                send_mail(subject, message, 'your-email@example.com', subscribers)