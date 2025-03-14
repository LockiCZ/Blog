from django.urls import path

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('quote/create', views.CreateQuoteView.as_view(), name='quote_new'),

    path('blog/', views.BlogView.as_view(), name='blog'),

    path('services/', views.ServicesView.as_view(), name='services'),

    path('about/', views.ContactView.as_view(), name='contact'),

    path('faq/', views.FaqView.as_view(), name='FAQ'),

    path('post/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),

    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),

    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),

    path('user/login/', views.LoginView.as_view(), name='login'),
    path('user/logout/', views.LogoutView.as_view(), name='logout'),
    path('user/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('user/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('user/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('user/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
]
