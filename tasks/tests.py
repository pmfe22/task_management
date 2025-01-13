from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Task
from django.utils import timezone

class TaskViewsTestCase(TestCase):

    def setUp(self):
        # ایجاد یک کاربر برای ورود
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # ایجاد یک وظیفه برای تست صفحه task list
        self.task = Task.objects.create(
            title="Test Task",
            description="Test Description",
            created_by=self.user,
            due_date=timezone.now()
        )

    def test_task_list_view(self):
        # تست اینکه آیا صفحه task_list به درستی بارگذاری می‌شود
        self.client.login(username='testuser', password='12345')  # ورود به سیستم
        response = self.client.get(reverse('task_list'))  # ارسال درخواست GET به صفحه task_list
        self.assertEqual(response.status_code, 200)  # بررسی وضعیت HTTP 200
        self.assertContains(response, "Test Task")  # بررسی اینکه وظیفه مورد نظر در صفحه نمایش داده می‌شود

    def test_create_task_view(self):
        # تست اینکه آیا صفحه create_task به درستی فرم را ارسال می‌کند
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('create_task'))
        self.assertEqual(response.status_code, 200)  # بررسی وضعیت HTTP 200

        # ارسال فرم بدون پر کردن فیلدها برای ایجاد یک وظیفه
        response = self.client.post(reverse('create_task'), {
            'title': '',  # فیلد عنوان خالی است
            'description': '',  # فیلد توضیحات خالی است
            'status': 'todo',  # وضعیت درست است
            'due_date': timezone.now(),  # اضافه کردن تاریخ
        })

        # بررسی اینکه پیغام خطا برای فیلدهای خالی نمایش داده می‌شود
        self.assertContains(response, 'This field is required')  # بررسی پیام خطا برای فیلدهای required
        self.assertEqual(Task.objects.count(), 1)  # تعداد وظایف نباید تغییر کند

        # ارسال فرم با پر کردن همه فیلدها
        response = self.client.post(reverse('create_task'), {
            'title': 'New Task',
            'description': 'New Task Description',
            'status': 'todo',  # وضعیت به درستی ارسال می‌شود
        })

        # بررسی اینکه بعد از ارسال فرم، تعداد وظایف افزایش یافته و به صفحه task_list هدایت می‌شود
        self.assertEqual(Task.objects.count(), 2)  # تعداد وظایف باید یک افزایش داشته باشد
        self.assertRedirects(response, reverse('task_list'))  # بررسی اینکه بعد از ارسال به صفحه task_list هدایت می‌شود
