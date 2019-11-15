from django.shortcuts import render, HttpResponse
import random

# Create your views here.
def pick_lotto(request):
    lotto = random.sample(range(1, 46), 6)
    return render(request, 'pick_lotto.html', { 'lotto': lotto })
    
def square(request, n):
    result = (int(n) ** 2)
    return  render(request, 'square.html', { 'num': int(n),'result': result })