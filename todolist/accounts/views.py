# accounts/views.py

# 장고 기본 기능
from django.urls import reverse_lazy
from django.views import generic
# forms, models 모듈 임포트
from django import forms 
from django.forms import ModelForm # ModelForm 사용을 위해 임포트
from django.contrib.auth.models import User # User 모델 import (필요시)

# Todo List 관련 Import
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Todo # 🚨 Todo 모델을 import 해야 합니다.

# 회원가입 관련 Import
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.password_validation import validate_password # 비밀번호 유효성 검사기

# ----------------------------------------------------------------------
# 1. [회원가입 폼]: 한글 레이블 및 유효성 검사 메시지 적용
# ----------------------------------------------------------------------
class KoreanUserCreationForm(UserCreationForm):
    # ... (이전에 수정했던 회원가입 폼 클래스 내용 유지) ...
    # 1. 사용자 이름 (username) 필드 한글화
    username = forms.CharField(
        max_length=150,
        label='사용자 이름',
        help_text='150자 이하로 설정해 주세요. 문자, 숫자, @ / . / + / - / _ 만 사용 가능합니다.',
    )

    # 2. 비밀번호 (password) 필드 한글화
    password = forms.CharField(
        label='비밀번호',
        widget=forms.PasswordInput,
        help_text='최소 8자 이상이어야 하며, 개인 정보와 무관한 안전한 비밀번호를 사용하세요.',
        validators=[validate_password] 
    )
    
    # 3. 비밀번호 확인 (password2) 필드 한글화
    password2 = forms.CharField(
        label='비밀번호 확인',
        widget=forms.PasswordInput,
        help_text='인증을 위해 위에 입력한 비밀번호와 동일하게 입력해 주세요.',
    )
    
    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields 

# ----------------------------------------------------------------------
# 2. [Todo 폼]: forms.py 없이 ModelForm 정의
# ----------------------------------------------------------------------

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'is_completed']
        
        # [핵심 수정]: Textarea 위젯 적용 및 한글 레이블 지정
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'title': '제목',
            'description': '상세 설명',
            'is_completed': '완료 여부',
        }
        # help_texts를 필요하다면 추가할 수 있습니다.
        # help_texts = { 'is_completed': '할 일을 완료했으면 체크하세요.' }
        

# ----------------------------------------------------------------------
# 3. 뷰 클래스 수정 (Todo 폼 사용)
# ----------------------------------------------------------------------

class SignUpView(generic.CreateView):
    form_class = KoreanUserCreationForm 
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'


# 1. Todo List 목록 조회 (Read: List)
class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Todo
    template_name = 'accounts/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

# 2. Todo 생성 (Create)
class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Todo
    # fields = ['title', 'description', 'is_completed']  <-- 삭제하고 form_class 사용
    form_class = TodoForm # <--- 정의한 TodoForm 사용
    template_name = 'accounts/todo_add.html' # 파일명에 맞춰 수정
    success_url = reverse_lazy('accounts:list') 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# 3. Todo 수정 (Update)
class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Todo
    # fields = ['title', 'description', 'is_completed']  <-- 삭제하고 form_class 사용
    form_class = TodoForm # <--- 정의한 TodoForm 사용
    template_name = 'accounts/todo_form.html'
    success_url = reverse_lazy('accounts:list')

    def test_func(self):
        todo = self.get_object()
        return todo.user == self.request.user

# 4. Todo 삭제 (Delete)
class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Todo
    template_name = 'accounts/todo_confirm_delete.html'
    success_url = reverse_lazy('accounts:list')

    def test_func(self):
        todo = self.get_object()
        return todo.user == self.request.user
