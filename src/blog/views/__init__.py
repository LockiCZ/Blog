from .views import (
    HomeView,
    ServicesView,
    ContactView,
    FaqView,
    BlogView,
)
from .auth_views import (
    UserProfileView,
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordChangeView,
    PasswordChangeDoneView,
)
from .post_views import (
    CreatePostView,
    PostUpdateView,
    PostDeleteView,
    post_detail,
)
from .comment_views import (
    add_comment_to_post,
    comment_approve,
    comment_remove,
)
from .sigle_form_views import CreateQuoteView
from .martor_views import martor_uploader
