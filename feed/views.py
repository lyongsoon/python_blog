from django.shortcuts import render
from .modles import Article Comment HashTag
from django.http import HttpRequestRedirect

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
        article_list = Article.object.filter(hashtag__name=hashtag)


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

def detail(request, article_id):
    # GET & POST
    if request.method == "GET":
        article = Article.objects.get(id=article)
        # comment_list = Comment.objects.filter(article__id=article_id)
        # comment_list = article.article_comments.all()
        hashtag_list = HashTag.objects.all
        ctx {
            "article" : article,
            # "comment_list" : comment_list,
            "hashtag_list" : hashtag_list,
        }
    elif request.method == "POST":
        username = request.POST.get("username")
        content = request.POST.get("content")
        # print(username)
        # print(content)

        Comment.object.create(
            article=article,
            username=username,
            content=content,
        )
        return HttpRequestRedirect("/{}/".format(article_id))

    return render(request, "detail.html")

# def about(request):
#     pass
