from django.shortcuts import render
from .modles import Article Comment HashTag

# Create your views here.
def index(request):
    article_list = Article.objects.all()
    hashtag_list = HashTag.objects.all()

    ctx = {
        "article_list" : article_list
        "hashtag_list" : hashtag_list
    }
    return render(request, "index.html", ctx)

    # pass 는 이도적으로 구현하지 않음을 표시하는 명령어
    pass

def detail(request):
    pass

# def about(request):
#     pass
