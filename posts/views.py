from django.shortcuts import render

from rest_framework import status


from rest_framework.decorators import api_view, action
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.response import Response 
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework import generics

from .models import Post, Commnet
from .serializers import PostBaseModelSerializer, PostListModelSerializer, PostRetrieveModelSerializer


#게시물 목록 + 생성(createAPIView)
class PostListCreateView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        #self.perform_create(serializer)
        instance = serializer.save(writer=request.user)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


#게시글 상세, 수정, 삭제
class PostRetrieveUpdateView(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostRetrieveModelSerializer


class PostModelViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostListModelSerializer

    #권한 함수
    def get_permissions(self):
        permission_classes = list()
        action = self.action

        if action == 'list':
            permission_classes = [AllowAny]
        elif action == ['create', 'retrieve']:
            permission_classes = [IsAuthenticated]
        elif action == ['update','partial_update','destroy']:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes] 
    
    @action(detail=True, methods=['get'])
    def get_comment_all(self, request, pk=None):
        post = self.get_object()
        comment_all = post.set_comment.all()
        return Response()


@api_view()
def calculator(request):
    #데이터 확인
    num1 = request.GET.get('num1', 0)
    num2 = request.GET.get('num2', 0)
    operators = request.GET.get('operators')

    #계산
    if operators == '+':
        result = int(num1) + int(num2)
    elif operators =='-':
        result = int(num1) - int(num2)
    elif operators=='*':
        result = int(num1)*int(num2)
    elif operators == '/':
        result = int(num1)/int(num2)
    else:
        result = 0
    
    data = {
        'type': 'FBV', #함수 기반 뷰
        'result' : result,
    }

    #응답
    return Response(data)


class CalculatorAPIView(APIView):
    def get(self, request):
        
            #데이터 확인
        num1 = request.GET.get('num1', 0)
        num2 = request.GET.get('num2', 0)
        operators = request.GET.get('operators')

        #계산
        if operators == '+':
            result = int(num1) + int(num2)
        elif operators =='-':
            result = int(num1) - int(num2)
        elif operators=='*':
            result = int(num1)*int(num2)
        elif operators == '/':
            result = int(num1)/int(num2)
        else:
            result = 0
        
        data = {
            'type': 'CBV', #클래스 기반 뷰
            'result' : result,
        }
        return Response(data)
    
    def post(self, request):
        data = {
            'type':'CBV',
            'method': 'POST',
            'result':0,

        }
        return Response(data)