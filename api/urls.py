from django.urls import path
from . import views  # import the views module from the current package

urlpatterns = [
    # 'as_view()' is a method that returns a callable view function that takes a request and returns a response
    path('create/', views.CreatePostView.as_view(), name='create_post'),  # URL: /posts/create/
    path('get/<int:id>/', views.GetPostView.as_view(), name='get_post'),  # URL: /posts/get/<id>/
    path('get/', views.GetAllPostsView.as_view(), name='get_all_posts'),  # URL: /posts/get/
    path('update/<int:id>/', views.UpdatePostView.as_view(), name='update_post'),  # URL: /posts/update/<id>/
    path('delete/<int:id>/', views.DeletePostView.as_view(), name='delete_post'),  # URL: /posts/delete/<id>/
]