from django.shortcuts import render , get_object_or_404 , redirect
from rest_framework import generics, permissions, viewsets , serializers
from rest_framework.response import Response 
from .models import Task
from .serializers import TaskSerializer
from django.views import View
from django.views.generic import ListView , CreateView
from django.urls import reverse_lazy
from .forms import TaskForm
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # استفاده از کاربر وارد شده برای پر کردن created_by
        serializer.save(created_by=self.request.user)


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]

    # متد برای ایجاد یک وظیفه جدید
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    # متد برای به‌روزرسانی کامل وظیفه
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        # جلوگیری از تغییر فیلد created_by
        if 'created_by' in request.data:
            request.data['created_by'] = instance.created_by.id  # حفظ مقدار قبلی
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    # متد برای به‌روزرسانی جزئی وظیفه
    def partial_update(self, request, *args, **kwargs):
        instance = self.get_object()
        # جلوگیری از تغییر فیلد created_by
        if 'created_by' in request.data:
            request.data['created_by'] = instance.created_by.id  # حفظ مقدار قبلی
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        ref_name = 'TaskViewSerializer'


@method_decorator(login_required, name='dispatch')
class CreateTaskView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('task_list')  # مسیر هدایت به لیست تسک‌ها

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # تنظیم کاربر ایجادکننده به کاربر فعلی
        return super().form_valid(form)
    

@method_decorator(login_required, name='dispatch')  
class EditTaskView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/edit_task.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user  # جلوگیری از تغییر کاربر ایجادکننده
        return super().form_valid(form)

# صفحه جزئیات وظیفه
# @method_decorator(login_required, name='dispatch')  
class TaskDetailView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'tasks/task_detail.html', {'task': task})
    

class TaskListView(ListView):
    model = Task
    template_name = 'tasks/task_list.html'  # مسیر فایل template
    context_object_name = 'tasks'     


@method_decorator(login_required, name='dispatch')
class DeleteTaskView(View):
    def get(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        return render(request, 'tasks/delete_task.html', {'task': task})

    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.delete()
        return redirect(reverse_lazy('task_list'))  # پس از حذف، به لیست وظایف برگشت    