from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Category, Post, Register

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PostSerializer2(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False) #from StringRelatedField we can read only
    # category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='category_detail')
    # category = serializers.HyperlinkedRelatedField(many=False, queryset=Category.objects.all(), view_name='category_detail')
    # Category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")
    owner = serializers.ReadOnlyField(source='owner.username')
    # owner = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'body', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    # posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
    posts = PostSerializer2(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'posts']

class PostSerializer1(serializers.ModelSerializer):
    # category = serializers.StringRelatedField(many=False) #from StringRelatedField we can read only
    # category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='category_detail')
    # category = serializers.HyperlinkedRelatedField(many=False, queryset=Category.objects.all(), view_name='category_detail')
    # Category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'owner', 'title', 'body', 'created_at', 'updated_at']

class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer1(many=True, read_only=True, source='post_set')
    class Meta:
        model = Category
        fields = ['title', 'created_at', 'posts', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField(many=False) #from StringRelatedField we can read only
    # category = serializers.HyperlinkedRelatedField(many=False, read_only=True, view_name='category_detail')
    # category = serializers.HyperlinkedRelatedField(many=False, queryset=Category.objects.all(), view_name='category_detail')
    # Category = serializers.SlugRelatedField(many=False, read_only=True, slug_field="title")# it is readable or writable
    owner = serializers.ReadOnlyField(source='owner.username')
    url = serializers.HyperlinkedIdentityField(many=False, view_name='category_detail', read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'url', 'category', 'owner', 'title', 'body', 'created_at', 'updated_at']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Register
        fields = ['name', 'email', 'phone', 'username', 'password']
