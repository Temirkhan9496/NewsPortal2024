from django.shortcuts import render, get_object_or_404, redirect
from news.models import Article
from news.forms import SubscriptionForm
from django.contrib.auth.decorators import login_required

def index(request):
    articles = Article.objects.all()
    return render(request, 'news/index.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'news/article_detail.html', {'article': article})

@login_required
def subscribe(request):
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            subscription = form.save(commit=False)
            subscription.user = request.user
            subscription.save()
            return redirect('index')
    else:
        form = SubscriptionForm()
    return render(request, 'news/category_subscription.html', {'form': form})