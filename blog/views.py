from django.shortcuts import render

# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html', {})

'''
방금 post_list 라는 함수는 요청(request) 을 넘겨받아 render 메서드를 호출합니다. 이 함수는
render 메서드를 호출하여 받은(return) blog/post_list.html 템플릿을 보여줍니다.

'''