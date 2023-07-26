from django.db import models
from django.contrib.auth import get_user_model #장고에서 사용하고있는 유저 모델을 가져오는 명령어
#모델링을 해야한다.

User = get_user_model()

class Post(models.Model): #models 안에 있는 Model 클래스를 상속받는 것.
    image = models.ImageField(verbose_name='이미지',null=True,blank=True)
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수', default=0)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True,blank=True)

class Commnet(models.Model):
    content = models.TextField(verbose_name='내용')
    created_at = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    post = models.ForeignKey(to='Post', on_delete=models.CASCADE)
    writer = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True,blank=True)
