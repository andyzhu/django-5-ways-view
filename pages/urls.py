from django.urls import path
from django.views.generic.base import TemplateView

from .views import (
    HomePageView,
    home_page_view_function_based,
    home_page_view_no_template,
    HomeDetailView,
)

urlpatterns = [
    path('home1/', HomePageView.as_view(), name='home1'), # 1. App + TemplateView
    path('home2/', home_page_view_function_based, name='home2'), # 2. Function Based View
    path('home3/', home_page_view_no_template, name='home3'), # 3. No Template View
    # path('home4/', TemplateView.as_view(template_name = 'pages/home_no_app.html'), name='home4'), # 4. No App, direct at urls.py
    path('home5/<int:pk>/', HomeDetailView.as_view(), name='post_detail') # 5. Model based View
]