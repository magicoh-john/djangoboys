from django.urls import path

# 장고 함수인 path 와 blog 애플리케이션에서 사용할 모든 views 를 import함(가져옴)
from . import views

# 첫 번째 URL 패턴을 추가
urlpatterns = [
    path('', views.post_index, name='post_index'),
    path('list', views.post_list, name='post_list'),
]

'''
['', views.post_list]
이제 post_list 라는 view 가 루트 URL에 할당되었습니다.
이 URL 패턴은 빈 문자열에 매칭이 되며, 장고 URL 확인자(resolver)
는 전체 URL 경로에서 접두어(prefix)에 포함되는 도메인 이름(i.e. http://127.0.0.1:8000/)을 무시하고 받아들입니다. 이 패턴은 장
고에게 누군가 웹사이트에 'http://127.0.0.1:8000/' 주소로 들어왔을 때 views.post_list 를 보여주라고 말해줍니다.

[name='post_list']
마지막 부분인 name='post_list' 는 URL에 이름을 붙인 것으로 뷰를 식별합니다. 뷰의 이름과 같을 수도 완전히 다를 수도 있습니
다. 이름을 붙인 URL은 프로젝트의 후반에 사용할 거예요. 그러니 앱의 각 URL마다 이름 짓는 것은 중요합니다. URL에 고유한 이
름을 붙여, 외우고 부르기 쉽게 만들어야 해요

'''