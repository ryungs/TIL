from django.shortcuts import render, HttpResponse, redirect
from .models import Article
# from django.views.decorators.csrf import csrf_exempt

# 처음 Create
# # user가 입력하는 창(html)
# def new(request):
#     return render(request, 'boards/new.html')

# # user가 넘긴 데이터를 실제 DB에 저장하는 액션
# # @csrf_exempt -> csrf 방어를 해제
# def create(request):
#     input_title = request.POST.get('input_title')
#     input_content = request.POST.get('input_content')
    
#     article = Article(title=input_title, content=input_content)
#     article.save()
#     # return HttpResponse(200)
#     return redirect(f'/boards/articles/{article.id}')

# 최종 Create
def new_article(request):
    # Get 요청일 때는, html을 보여준다
    if request.method == 'GET':
        return render(request, 'boards/new.html')
    
    # Post 요청일 때는, DB에 저장하고 redirect
    else:
        input_title = request.POST.get('input_title')
        input_content = request.POST.get('input_content')
    
        article = Article(title=input_title, content=input_content)
        article.save()
        # return HttpResponse(200)
        return redirect(f'/boards/articles/{article.id}')
    
    
    
# Read
# index : 모든 article 들을 보여주는 html(목록)
def index(request):
    articles = Article.objects.all()
    return render(request, 'boards/index.html', {'articles': articles})
    
# 특정 article 을 보여주는 html(상세)
def detail(request, id):
    article = Article.objects.get(id=id)
    return render(request, 'boards/detail.html', {'article': article})

# Update # Create와 차이는 처음 만들 때는 비어있지만 Update하려면 차 있는 상태에서 만들어진다
def update_article(request, id):
    article = Article.objects.get(id=id) # if랑 else 코드 반복되서 밖으로 빼줌
    # HTML 보여주기
    if request.method == 'GET':
        return render(request, 'boards/edit.html', {'article': article})
    
    #수정하기    
    else:
        article.title = request.POST.get('input_title')
        article.content = request.POST.get('input_content')
        article.save()
        return redirect(f'/boards/articles/{article.id}/')
    

    
# Destory
# 특정 article을 삭제하는 액션
def delete(request, id):
    # Post 요청일 때는, 삭제, redircet
    if request.method == 'POST':
        article = Article.objects.get(id= id) # 앞에 있는 id
        article.delete()
        return redirect ('/boards/articles/')
    # 그 외는 삭제하
    else:
        return redirect(f'/boards/articles/{id}/')
