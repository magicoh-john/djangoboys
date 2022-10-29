from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404

# from 다음에 있는 마침표(.)는 현재 디렉토리 또는 애플리케이션
from .models import Post
from django.utils import timezone


# Create your views here.


# post_index 뷰(view)
def post_index(request):
    return render(request, 'blog/post_index.html', {})


# post_list 뷰(view)
def post_list(request):
    # posts 라는 쿼리셋 선언하면서 결과 받아옴
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


'''
방금 post_list 라는 함수는 요청(request) 을 넘겨받아 render 메서드를 호출합니다. 이 함수는
render 메서드를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.

'''


# 게시물 상세 페이지 처리 핸들러(뷰)
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
