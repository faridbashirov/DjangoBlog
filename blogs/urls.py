from django.urls import path
from .views import blog_detail,BlogListView,add_blog
urlpatterns = [
    path('blog_detail/<int:id>/', blog_detail,name="blog_detail"),
    path('blog_list/', BlogListView.as_view(),name="blog_list"),
    path('add_blog/', add_blog,name="add_blog"),
]
