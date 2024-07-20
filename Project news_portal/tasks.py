from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from news.models import Subscription, Article
from datetime import datetime, timedelta

@shared_task
def send_weekly_digest():
    week_ago = datetime.now() - timedelta(days=7)
    new_articles = Article.objects.filter(created_at__gte=week_ago)
    for subscription in Subscription.objects.all():
        articles_for_user = new_articles.filter(category=subscription.category)
        if articles_for_user.exists():
            subject = f'Weekly Digest for {subscription.category.name}'
            html_message = render_to_string('news/weekly_email.html', {'articles': articles_for_user})
            plain_message = strip_tags(html_message)
            send_mail(subject, plain_message, 'from@example.com', [subscription.user.email])