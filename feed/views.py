from django.shortcuts import render
from .modles import Article Comment HashTag

# Create your views here.
def index(request):

    # GET & POST
    category = request.GET.get("category")
    hashtag = request.GET.get("hashtag")

    hashtag_list = HashTag.objects.all()
    if not category and hashtag:
        article_list = Article.objects.All()
    elif:
        article_list = Article.objects.filter(category=category)
    else:
        article_list = Article.object.filter(hashtag=hashtag)
        

    # Case 1
    # category_list = set([])
    # for article in article_list:
    #     category_list.add(article.get_category_display())
    # print(category_list)

    # Case 2
    # category_list = set([
    #     article.get_category_display()
    #     for article in article_list
    # ])

    # Case 3
    category_list = set([
        (article.category, article.get_category_display())
        for article in article_list
    ])

    ctx = {
        "article_list" : article_list,
        "hashtag_list" : hashtag_list,
        "category_list" : category_list,
    }
    return render(request, "index.html", ctx)

    # # pass 는 이도적으로 구현하지 않음을 표시하는 명령어
    # pass

def detail(request):
    article = Article.objects.get(id=article)
    hashtag_list = HashTag.objects.all
    ctx {
        "article" : article,
        "hashtag_list" : hashtag_list,
    }
    return render(request, "detail.html")

# def about(request):
#     pass
