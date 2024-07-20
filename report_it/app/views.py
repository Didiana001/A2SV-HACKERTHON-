from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.db import IntegrityError
from .models import Authority, Report
from django.shortcuts import get_object_or_404

# Home View
class HomeView(View):
    def get(self, request):
        return render(request, 'app/home.html')

# Tracking View
@method_decorator(login_required, name='dispatch')
class TrackingView(View):
    def get(self, request):
        reports = Report.objects.filter(user=request.user)
        return render(request, 'app/tracking.html', {'reports': reports})

# Registration View
class RegistrationView(View):
    def get(self, request):
        return render(request, 'app/registration.html')

    def post(self, request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            return render(request, 'registration.html', {
                'error': 'Passwords do not match.'
            })

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('home')
        except IntegrityError:
            return render(request, 'app/registration.html', {
                'error': 'Username already exists. Please choose another username.'
            })

# Login View
class LoginView(View):
    def get(self, request):
        return render(request, 'app/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'app/login.html', {'error': 'Invalid credentials'})

# Authority Views
class AuthorityListView(View):
    def get(self, request):
        authorities = Authority.objects.all()
        return render(request, 'app/authority_list.html', {'authorities': authorities})

class AuthorityDetailView(View):
    def get(self, request, pk):
        authority = get_object_or_404(Authority, pk=pk)
        return render(request, 'app/authority_detail.html', {'authority': authority})

# Report Views
class ReportListView(View):
    def get(self, request):
        reports = Report.objects.all()
        return render(request, 'app/report_list.html', {'reports': reports})

class ReportDetailView(View):
    def get(self, request, pk):
        report = get_object_or_404(Report, pk=pk)
        return render(request, 'app/report_detail.html', {'report': report})

@method_decorator(login_required, name='dispatch')
class ReportCreateView(View):
    def get(self, request):
        return render(request, 'app/report_form.html')

    def post(self, request):
        title = request.POST['title']
        location = request.POST['location']
        report_type = request.POST['report_type']
        description = request.POST['description']
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        report = Report.objects.create(
            title=title,
            location=location,
            report_type=report_type,
            description=description,
            image=image,
            video=video,
            user=request.user
        )

        return redirect('app/report_detail', pk=report.pk)
