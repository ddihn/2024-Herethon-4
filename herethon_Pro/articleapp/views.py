from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from .models import Article

@login_required
def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        position = request.POST.get('position')
        keyword = request.POST.get('keyword')
        keyword2 = request.POST.get('keyword2')
        keyword3 = request.POST.get('keyword3')
        content = request.POST.get('content')
        user = request.user

        # Article 객체 생성 및 저장
        article = Article.objects.create(
            user=user,
            name=name,
            position=position,
            content=content,
            keyword=keyword,
            keyword2=keyword2,
            keyword3=keyword3,

        )
        # 생성된 글의 detail 페이지로 리디렉션
        return redirect('articleapp:detail')
    return render(request, 'articleapp/create.html')

@login_required
@require_http_methods(["GET", "POST"])

def detail(request):
    articles = Article.objects.filter(user=request.user).order_by('-id') 
    return render(request, 'articleapp/detail.html', {'articles': articles})

def detail2(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articleapp/article_list.html', {'article' : article})