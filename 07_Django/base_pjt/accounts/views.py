from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
# Create your views here.

def index(request):
    return render(request, 'accounts/index.html')

def signup(request):
    # 사용자가 실제 데이터를 제출했다면 저장한 다음에
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:index')
    # 사용자가 가입하겠다고 들어오면 보여줄 html
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
    })

def signin(request):
    # 이미 로그인 했는데 또 로그인 한다하면,
    if request.user.is_authenticated:
        return redirect('accounts:index')

    # 로그인 시켜주세요
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid(): # 검증 성공
            login(request, form.get_user()) # 로그인 하고

            if request.GET.get('next'): # 이전에 있던 페이지가 있다면
                return redirect(request.GET.get('next'))
            return redirect('accounts:index')
    # 로그인 화면주세요
    else:
        form = AuthenticationForm
    return render(request, 'accounts/signup.html',{
      'form':form
    })

def signout(request):
    logout(request)
    return redirect('accounts:index')






