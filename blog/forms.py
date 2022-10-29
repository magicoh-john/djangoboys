from django import forms
from .models import Post


# PostForm : 만들 폼의 이름(Post Model과 연결되는 폼이다.)
# forms.ModelForm 은 장고에게 이 폼이 ModelForm이라는 것을 알려주는 역할
class PostForm(forms.ModelForm):

    # 이 폼을 만들기 위해서 어떤 model이 쓰여야 하는지 장고에 알려주는 역할
    class Meta:
        model = Post
        fields = ('title', 'text',)
