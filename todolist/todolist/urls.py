from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # 로그인/로그아웃 기본 제공
    path('accounts/', include('accounts.urls')),             # 회원가입(커스텀)
    path('', include('todo.urls')),
]

