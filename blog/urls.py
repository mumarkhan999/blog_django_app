from django.urls import path

from .import views

urlpatterns = [
    path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
    path('', views.BlogListView.as_view(), name='home'),
]


# A common way of development is first make a
# url
# then a template
# then a view
# and that's it
