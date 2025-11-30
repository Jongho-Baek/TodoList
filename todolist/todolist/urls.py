# config/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 🚨 수정: accounts 앱의 모든 URL은 'accounts/' 경로 아래에 위치하도록 변경
    path('accounts/', include('accounts.urls')), 
    
    # 루트 경로("/")로 접근 시 Todo 목록 페이지(login 필요)로 리다이렉트 
    # 또는 login 페이지로 리다이렉트
    path('', RedirectView.as_view(pattern_name='accounts:list', permanent=False)),
]
