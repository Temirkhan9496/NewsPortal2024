from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Post
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=category)
    subscribed = False
    if request.user.is_authenticated:
        subscribed = category.subscribers.filter(id=request.user.id).exists()
    return render(request, 'news/category_detail.html',
                  {'category': category, 'posts': posts, 'subscribed': subscribed})


@login_required
def subscribe_to_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.subscribers.add(request.user)
    messages.success(request, f'You have subscribed to {category.name} category.')
    return redirect('category_detail', pk=category.pk)