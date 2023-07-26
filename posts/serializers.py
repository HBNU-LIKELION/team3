from rest_framework.serializers import ModelSerializer

from .models import Post, Commnet

class PostBaseModelSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        #fields = ['id','content','view_count']

class PostListModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['id','image','created_at','view_count','writer']
        #exclude = ['content',]
        depth = 1

class PostRetrieveModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        depth = 1



class PostCreateModelSerializer(PostBaseModelSerializer):
    class Meta(PostBaseModelSerializer.Meta):
        fields = ['image','content']
        
class PostDeleteModelSerializer(PostBaseModelSerializer):
    pass


class CommentListModelSerializer(ModelSerializer):
    class Meta:
        model = Commnet
        fields = '__all__'

