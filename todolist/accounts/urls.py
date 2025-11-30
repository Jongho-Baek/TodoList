# accounts/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views

# 🚨 해결책: 'views'라는 이름으로 현재 앱의 views.py 파일을 가져옵니다.
from . import views 

app_name = 'accounts'

urlpatterns = [
    # ----------------------------------------------------
    # 1. 인증 관련 URL
    # ----------------------------------------------------
    
    # 회원가입: views.py에서 구현한 SignUpView 사용
    path('signup/', views.SignUpView.as_view(), name='signup'),
    
    # 로그인: 장고 기본 뷰 사용
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    
    # 로그아웃: 장고 기본 뷰 사용
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # ----------------------------------------------------
    # 2. Todo List CRUD URL
    # ----------------------------------------------------
    
    # 목록 조회: 모든 뷰 앞에 'views.' 접두어를 붙여 오류를 해결합니다.
    path('', views.TodoListView.as_view(), name='list'),

    # 생성
    path('create/', views.TodoCreateView.as_view(), name='create'),

    # 수정 (PK 필요)
    path('<int:pk>/update/', views.TodoUpdateView.as_view(), name='update'),

    # 삭제 (PK 필요)
    path('<int:pk>/delete/', views.TodoDeleteView.as_view(), name='delete'),
]
