from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

from .views import (
    HomeView,
    TrackingView,
    RegistrationView,
    LoginView,
    AuthorityListView,
    AuthorityDetailView,
    ReportListView,
    ReportDetailView,
    ReportCreateView
)

urlpatterns = [
    # Home URL
    path('', HomeView.as_view(), name='home'),
    
    # Tracking URL
    path('tracking/', TrackingView.as_view(), name='tracking'),
    
    # Registration and Login URLs
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    
    # Authority URLs
    path('authorities/', AuthorityListView.as_view(), name='authority_list'),
    path('authorities/<int:pk>/', AuthorityDetailView.as_view(), name='authority_detail'),
    
    # Report URLs
    path('reports/', ReportListView.as_view(), name='report_list'),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report_detail'),
    path('reports/new/', ReportCreateView.as_view(), name='report_create'),

    # Logout URL
    path('logout/', LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)