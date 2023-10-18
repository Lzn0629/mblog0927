from django.shortcuts import render
from django.http import HttpResponse
from mysite.models import Post
from datetime import datetime
from django.shortcuts import redirect


# Create your views here.
def homepage(request):
    posts = Post.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
	try:
		post = Post.objects.get(slug = slug)
		if post != None:
			return render(request, 'post.html', locals())
	except:
		return redirect('/')


'''
def homepage(request): #定義函式
    posts = Post.objects.all()
    post_lists = list() #動態陣列
    for counter, post in enumerate(posts): #enumerate 自動數有幾筆
        post_lists.append(f'No.{counter}-{post} <br>')  #br 網頁的換行 #f格式化
    return HttpResponse(post_lists)
'''