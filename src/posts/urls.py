from django.conf.urls.static import static
from django.urls import path

from blog import settings
from posts.views import BlogHome, BlogPostCreate, BlogPostEdit, BlogPostDetail, BlogPostDelete

app_name = 'posts'

urlpatterns = [
    path('', BlogHome.as_view(), name='home'),
    path('create/', BlogPostCreate.as_view(), name='create'),
    path('edit/<slug:slug>/', BlogPostEdit.as_view(), name='edit'),
    path('view/<slug:slug>/', BlogPostDetail.as_view(), name='view'),
    path('delete/<slug:slug>/', BlogPostDelete.as_view(), name='delete'),
]
