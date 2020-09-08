from rest_framework import serializers 
import json
from .models import Post , Profile , Coment , PostsRatting , Relationship ,Category
from django.contrib.auth.models import User

class RecursiveSerializer(serializers.Serializer):

	def to_representation(self, value):

		serializer = self.parent.parent.__class__(value, context=self.context)

		return serializer.data

class UserSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = User
		fields='__all__'

# https://concisecoder.io/2018/12/23/how-to-optimize-your-django-rest-viewsets/
# here is th useful data about serializers and smth select_related


class ProfileDetailSerializer(serializers.ModelSerializer):

	user = serializers.SerializerMethodField()

	def get_user(self,instance):

    	 return User.objects.filter(id=instance.user.id).values_list('username','email','date_joined')


	substo = serializers.SerializerMethodField()

	def get_substo(self ,instance):


		users = Relationship.objects.filter(user1=instance).prefetch_related('user2')

		vacab = {}

		for user in users:
			user = {
				user.user2.user.id: {
				'user': user.user2.user.first_name,
				'id': user.user2.user.id,
				'username': user.user2.user.username,
				'about': user.user2.about,
				}
			}

			vacab.update(user)
			
		return vacab

	# 	serializers.SlugRelatedField(
        #     many=True,
        #     read_only=True,
        #     slug_field="about",
        # )

	class Meta:
		model = Profile
		fields = "__all__"


class PostListSerializer(serializers.ModelSerializer):

	author = serializers.SerializerMethodField('get_author')

	category = serializers.SlugRelatedField(slug_field="name" , read_only = True , many=True)

	rating_user = serializers.BooleanField()

	middle_star = serializers.IntegerField()

	class Meta:
		model = Post
		fields = ('id', 'author', 'title', 'content', 'category' , 'rating_user', 'middle_star')

	def get_author(self , instance):
		
		return Profile.objects.filter(id = instance.author.id).select_related('user').values_list('user__username','about')


class PostSecondListSerializer(serializers.ModelSerializer):
	
	author = serializers.SerializerMethodField('get_author')

	category = serializers.SlugRelatedField(slug_field="name" , read_only = True , many=True)

	rating_user = serializers.BooleanField()

	middle_star = serializers.IntegerField()	

	class Meta:
		model = Post
		fields = ('id','author','title', 'content', 'category' , 'rating_user', 'middle_star','date_created')

	def get_author(self , instance):
		
		return Profile.objects.filter(id = instance.author.id).select_related('user').values_list('user__username','about')



class FilterComentListSerializer(serializers.ListSerializer):

	def  to_representation(self,data):
		
		data = data.filter(parent=None)
		
		return super().to_representation(data)


class ComentCreateSerializer(serializers.ModelSerializer):


	class Meta:
		model = Coment
		fields =('content','post','parent','author')



class ComentSerializer(serializers.ModelSerializer):

	children = RecursiveSerializer(many=True)

	class Meta:

		list_serializer_class = FilterComentListSerializer

		model = Coment

		fields = ('author','content','post' , 'children')


class PostDetailSerializer(serializers.ModelSerializer):

	category = serializers.SlugRelatedField(slug_field="name" , read_only = True,many=True)
	
	author = ProfileDetailSerializer(many=False)

	coments = ComentSerializer(many=True)
	
	class Meta:
		model = Post
		fields = "__all__"


class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
   
    class Meta:
        model = PostsRatting
        fields = ("star", "post")

    def create(self, validated_data):
        rating , _= PostsRatting.objects.update_or_create(
            ip=validated_data.get('ip', None),
            post=validated_data.get('post', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


class ProfileListSerializer(serializers.ModelSerializer):

	user = serializers.SerializerMethodField()

	def get_user(self, instance):

		return Profile.objects.filter(user__id=instance.user.id).prefetch_related('user').values_list('user__username')


	class Meta:
		model = Profile
		fields = "__all__"


class CreatePostSerializer(serializers.ModelSerializer):


	class Meta:
		model = Post
		fields = "__all__"


	def create(self, validated_data):
    
		return Post.objects.create(**validated_data)

class CategorySerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Category
		fields = '__all__'


class PostUpdateSerializer(serializers.ModelSerializer):

	category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True,many=True)

	class Meta:
		model = Post
		fields = '__all__'


	def partial_update(self,instance,validated_data):

		instance.title = validated_data.get('title', instance.title)
		
		instance.content = validated_data.get('content', instance.content)
		
		instance.bannerpic = validated_data.get('bannerpic', instance.bannerpic)

		instance.save()

		instance.category.set(validated_data.pop('category'))

		#remember forever dont make this mistake when data is manytomany use obj.set() instead of .save()
        
		return instance
