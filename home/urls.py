from django.contrib import admin
from django.urls import path
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.index, name='index'),
    path('main', views.main, name='main'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    # path('Signup', views.Signup, name='Signup'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('product/<int:id>/', views.view_detail, name='view_detail'),
    # path('Login', views.Login),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout'),
    path('donor/<int:id>/', views.donor, name='donor'),
    path('donor', views.donor, name='donor_new'), 
    path('patient', views.patient, name='patient'),
    path('view_detail', views.view_detail),
    path('thankyou', views.thankyou),
    path('status', views.status, name='status'),
    # path('upd',views.upd),



    
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)