# from django.urls import path
# from . import views
# from django.conf import settings
# from django.conf.urls.static import static
# from django.contrib.auth import views as auth_view
# from .forms import LoginForm, MyPasswordResetForm



# urlpatterns = [
#     path('', views.home),
#     path('about/',views.about,name='about'),
#     path('contact/',views.contact,name='contact'),
#     path('category/<slug:val>', views.CategoryView.as_view(),name="category"),
#     path('category-title/<val>', views.CategoryTitle.as_view(),name="category-title"),
#     path('product-detail/<int:pk>', views.ProductDetail.as_view(),name="product-detail"),
    

# #login authentication
# path('registration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
# path('accounts/login/',auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'), #auth_view is the another buildin module in authentication moodule
# path('password-reset/',auth_view.PasswordResetView.as_view
# (template_name= 'app/password_reset.html', form_class=MyPasswordResetForm),
# name='password_reset'),

# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_view
from .forms import LoginForm, MyPasswordResetForm

urlpatterns = [
    path('', views.home),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('category/<slug:val>', views.CategoryView.as_view(), name="category"),
    path('category-title/<val>', views.CategoryTitle.as_view(), name="category-title"),
    path('product-detail/<int:pk>', views.ProductDetail.as_view(), name="product-detail"),
    
    # login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    
    # password reset
    path('password-reset/', auth_view.PasswordResetView.as_view(
        template_name='app/password_reset.html',
        form_class=MyPasswordResetForm
    ), name='password_reset'),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(
        template_name='app/password_reset_done.html'
    ), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(
        template_name='app/password_reset_confirm.html'
    ), name='password_reset_confirm'),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(
        template_name='app/password_reset_complete.html'
    ), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
