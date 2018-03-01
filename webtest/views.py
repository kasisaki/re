from django.shortcuts import render

def reram(request):
    return render(request, 'webtest/index.html', {})

def post_list(request):
    return render(request, 'webtest/post_list.html', {})




# Create your views here.
