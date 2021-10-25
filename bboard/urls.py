from django.urls import path

from .views import index, by_rubric, BbCreateView, BbDetailView, BbByRubricView, blog, delete

urlpatterns = [
    path('detail/<int:pk>/', BbDetailView.as_view(), name='detail'),
    path('<int:rubric_id>/', BbByRubricView.as_view(), name='by_rubric'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('delete/<int:post_pk>/', delete, name='post_delete'),
    path('blog', blog, name='blog'),

    path('', index, name='index')
]


