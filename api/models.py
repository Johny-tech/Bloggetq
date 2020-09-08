import os
from django.db import models
import hashlib
from functools import partial
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
#manager are heree ok??


def hash_file(file, block_size=65536):
	hasher = hashlib.md5()
	for buf in iter(partial(file.read, block_size), b''):
		hasher.update(buf)

	return hasher.hexdigest()


def upload_profile_to(instance, filename):

	instance.profilepic.open()

	filename_base, filename_ext = os.path.splitext(filename)

	return "{0}.{1}".format(hash_file(instance.profilepic), filename_ext)


def upload_banner_to(instance, filename):

	instance.bannerpic.open()

	filename_base, filename_ext = os.path.splitext(filename)

	return "{0}.{1}".format(hash_file(instance.bannerpic), filename_ext)





# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE ,related_name="user")
	about = models.CharField(max_length=200, null=True) 
	ip = models.CharField(max_length=16,null=True)
	profilepic = models.ImageField(default='code_review.jpeg', upload_to=upload_profile_to, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	substo=models.ManyToManyField("api.Profile",through="api.Relationship", verbose_name=("relations"))
	authority = models.ManyToManyField("api.Profile", through="api.Estimation", verbose_name=("pricedProfiles"),related_name='estimations')

	
	def hash_file(file, block_size=65536):
		hasher = hashlib.md5()
		for buf in iter(partial(file.read, block_size), b''):
			hasher.update(buf)

		return hasher.hexdigest()


	def upload_to(instance, filename):

		instance.profilepic.open()

		filename_base, filename_ext = os.path.splitext(filename)

		return "{0}.{1}".format(hash_file(instance.profilepic), filename_ext)





	def __str__(self):
		return self.user.username


		

#here is the  model which realises xow  one user can subscibte to others
class Relationship(models.Model):
	
	CATEGORY = (
		('free', 'free'),
		('pro','pro'),
		('premium', 'premium'),
	)
	user1 = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='subscriber')
	user2 = models.ForeignKey(Profile, on_delete=models.CASCADE,related_name='author')
	subtype = models.CharField(max_length=200, null=True, choices=CATEGORY)



class Category(models.Model):
	name = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	def __str__(self):

		return self.name


class Post(models.Model):
	author = models.ForeignKey(Profile, null=True, on_delete= models.SET_NULL)
	category=models.ManyToManyField(Category,blank=True,related_name="posts")
	title = models.CharField(max_length=300,null=True)
	content= models.CharField(max_length=1000, null=True)
	bannerpic = models.ImageField(default='code_review.jpeg',upload_to=upload_banner_to,null=True , blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	viewed = models.PositiveIntegerField(default=1,null=True)
	
	def __str__(self):
		return self.title


# relational table
class Estimation(models.Model):
	profile1 = models.ForeignKey(
		'api.Profile', null=True, blank=True, on_delete=models.CASCADE, related_name="profileof")
	profile2 = models.ForeignKey(
		'api.Profile', null=True, blank=True, on_delete=models.CASCADE, related_name='estmto')
	like = models.PositiveIntegerField(default=1, null=True)
	



class Coment(models.Model):
	author = models.ForeignKey(User, null=True, on_delete= models.SET_NULL)
	content = models.CharField(max_length=1000, null=True)
	post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL,related_name="coments")
	parent = models.ForeignKey("api.Coment", on_delete=models.CASCADE,null=True,blank=True,related_name='children')


class RattingStar(models.Model):
	value = models.SmallIntegerField(default=0)


class PostsRatting(models.Model):
	ip = models.CharField(max_length=15)
	star = models.ForeignKey(RattingStar, null=True , on_delete = models.CASCADE)
	post = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL,related_name="ratings")
