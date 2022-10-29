"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# http://127.0.0.1:8000/ 로 들어오는 모든 접속 요청을 blog.urls 로 전송해 추가 명령을 찾을 거예요.
urlpatterns = [
    # 장고는 admin/이라는 요청에 맞는 핸들러(메소드)를 view에서 찾게됨 #
    path("admin/", admin.site.urls),
    # 127.0.0.1/ 이런 형태의 기본 요청이 오면 blog앱의 urls.py파일로 위임시킨다. #

    path('blog/', include('blog.urls')),

]
