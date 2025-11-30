# accounts/views.py

# 장고 기본 기능
from django.urls import reverse_lazy
from django.views import generic

# Todo List 관련 Import
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Todo # 🚨 Todo 모델을 import 해야 합니다.

# 회원가입 관련 Import
from django.contrib.auth.forms import UserCreationForm # 기본 회원가입 폼

# ----------------------------------------------------------------------
# 회원가입 뷰 (현재 코드 유지)
# ----------------------------------------------------------------------

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # 회원가입 성공 후, 로그인 페이지로 이동합니다.
    success_url = reverse_lazy('accounts:login') # accounts 앱의 login URL로 변경하는 것이 좋습니다.
    template_name = 'accounts/signup.html' # 템플릿 경로를 accounts 앱 내로 변경하는 것이 좋습니다.


# 1. Todo List 목록 조회 (Read: List)
class TodoListView(LoginRequiredMixin, generic.ListView):
    model = Todo
    template_name = 'accounts/todo_list.html'
    context_object_name = 'todos'

    def get_queryset(self):
        # 현재 로그인된 사용자의 Todo만 필터링합니다. (핵심)
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

# 2. Todo 생성 (Create)
class TodoCreateView(LoginRequiredMixin, generic.CreateView):
    model = Todo
    fields = ['title', 'description', 'is_completed']
    template_name = 'accounts/todo_form.html'
    success_url = reverse_lazy('accounts:list') # Todo 목록 페이지로 이동

    def form_valid(self, form):
        # 저장 전, user 필드에 현재 로그인된 사용자 할당 (핵심)
        form.instance.user = self.request.user 
        return super().form_valid(form)

# 3. Todo 수정 (Update)
class TodoUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Todo
    fields = ['title', 'description', 'is_completed']
    template_name = 'accounts/todo_form.html'
    success_url = reverse_lazy('accounts:list')

    # 소유자만 수정 가능하도록 검사합니다.
    def test_func(self):
        todo = self.get_object()
        return todo.user == self.request.user

# 4. Todo 삭제 (Delete)
class TodoDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Todo
    template_name = 'accounts/todo_confirm_delete.html'
    success_url = reverse_lazy('accounts:list')

    # 소유자만 삭제 가능하도록 검사합니다.
    def test_func(self):
        todo = self.get_object()
        return todo.user == self.request.user
