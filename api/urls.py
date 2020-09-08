from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = format_suffix_patterns([
	# path('', views.apiOverview, name="api-overview"),
  	 path('posts/', views.PostViewSet.as_view({'get': 'list'})),
  	 path('post-create/', views.PostViewSet.as_view({'get':'create'})),
	 path('post-detail2/<int:pk>',views.getObject),
  	 path('post-update/<int:pk>',views.PostViewSet.as_view({'put':'partial_update'})),
  	 path('post-update3/<int:pk>',views.postUpdate),
  	 path('post-generic-list/',views.ListPostView.as_view()),
  	 path('post-recent/',views.PostViewSet.as_view({'get':'recent_posts'})),
  	 path('post-update2/<int:pk>',views.PostUpdateView.as_view()),
  	 path('coment-create/', views.ComentCreateView.as_view()),
	 path('post-detail/<int:pk>', views.PostViewSet.as_view({'get':'retrieve'})),
	 path('profile/<str:username>',views.ProfileViewSet.as_view({'get':'retrieve'})),
	 path('profiles/',views.ProfileViewSet.as_view({'get':'list'})),
  	 path('rating/', views.AddStarRatingViewSet.as_view({'post':'create'})),
    # url(r'^logout/$', auth_views.LogoutView, name='logout'),
	
	# path('posts/<str:pk>/', views.postDetail, name="post"),
	# path('post-create/', views.postCreate, name="post-create"),

	# path('post-update/<str:pk>/', views.postUpdate, name="post-update"),
	# path('post-delete/<str:pk>/', views.postDelete, name="post-delete"),
])
