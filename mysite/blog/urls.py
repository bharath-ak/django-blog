from django.urls import path
from blog import views

urlpatterns = [
    path('',views.PostListView.as_view(),name='post_list'),
    path('about/',views.AboutView.as_view(),name='about'),
    path('post/new',views.PostCreateView.as_view(),name='post_new'),
    path('post/<pk>',views.PostDetailView.as_view(),name='post_detail'),
    path('post/<pk>/update',views.PostUpdateView.as_view(),name='post_edit'),
    path('post/<pk>/delete',views.PostDeleteView.as_view(),name='post_remove'),
    path('post/<pk>/publish',views.post_publish,name='post_publish'),
    path('drafts/',views.DraftListView.as_view(),name='post_draft_list'),
    path('post/<pk>/comment',views.add_comment_to_post,name='add_comment_to_post'),
    path('comment/<pk>/approve',views.comment_approve,name='comment_approve'),
    path('comment/<pk>/delete',views.comment_delete,name='comment_remove')
]
