# Create your views here.

from django.shortcuts import get_object_or_404, render
from django.http import Http404
from .forms import CommentForm

from .models import News
from .models import Comment, Tag, Category

def get_news(request):
    ctx = {
        'news': News.objects.all().order_by('-created'),
        'tags': Tag.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'news/news-list.html', ctx)
'''
这里，我们使用了 Django 的 ORM 对博客数据进行查询，并依发布时间的倒序进行排列
然后将结果集（一个 QuerySet 对象）放在一个字典对象 ctx 的 news 中。
然后调用 render 方法来渲染模板，其第一个参数始终接收 request 对象，第二个参数是要渲染的模板文件，第三个参数则是可选的上下文参数。
注意观察视图函数的入参，其第一个参数一定是 request 对象，“这是一个不变的真理”。
'''

def get_detail(request, news_id):
    name = request.session.get('username','')
    try:
        news = News.objects.get(id=news_id)
    except News.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm(
            initial={'name': name}
        )
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['news'] = news
            Comment.objects.create(**cleaned_data)

    ctx = {
        'news': news,
        'comments': news.comment_set.all().order_by('-created'),
        'form': form,
        'tags': Tag.objects.all(),
        'category': Category.objects.all()
    }
    return render(request, 'news/news-detail.html', ctx)