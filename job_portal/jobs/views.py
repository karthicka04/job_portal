from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Job  # Keep this import for Job model
from .forms import JobForm
from .models import Job
CustomUser = get_user_model()

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'jobs/signup.html', {'form': form})

@login_required
def job_list_view(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def admin_dashboard_view(request):
    if request.user.is_superuser:
        users = CustomUser.objects.all()
        return render(request, 'jobs/admin_dashboard.html', {'users': users})
    else:
        return redirect('login')
def add_job_view(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            # Check if foreign key constraints are satisfied
            if job.some_foreign_key_field and not SomeModel.objects.filter(id=job.some_foreign_key_field.id).exists():
                form.add_error(None, "Foreign key constraint failed.")
            else:
                job.save()
                return redirect('success_url')
    else:
        form = JobForm()
    return render(request, 'jobs/add_job.html', {'form': form})
