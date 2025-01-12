from django.urls import path
from . import views

urlpatterns = [
    path("", views.uhome, name="uhome"),
    path("usignup/", views.usignup, name="usignup"),
    path("ulogin/", views.ulogin, name="ulogin"),
    path("ulogout/", views.ulogout, name="ulogout"),
    path("ucp/", views.ucp, name="ucp"),
    path("post/new/", views.post_create, name="post_new"),
    path("post/<int:pk>/edit/", views.post_update, name="post_edit"),
    path("post/<int:pk>/delete/", views.post_delete, name="post_delete"),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('post/<int:pk>/like/', views.like_post, name='like_post'),
]
