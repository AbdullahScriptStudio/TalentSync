from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm, CustomLoginForm
from django.contrib.auth.decorators import login_required


def register(request):
    """ Register a new user """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            
            # Clear fields based on user role
            if user.role == 'recruiter':
                user.resume = None  # Recruiters don't need resumes
            elif user.role == 'applicant':
                user.company_name = None  # Applicants don't need company names
            
            user.save()
            login(request, user)
            return redirect('dashboard_redirect')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'people/register.html', {'form': form})


def user_login(request):
    """ Login View """
    if request.method == 'POST':
        form = CustomLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard_redirect')
    else:
        form = CustomLoginForm()

    return render(request, 'people/login.html', {'form': form})

@login_required
def user_logout(request):
    """ Logout View """
    logout(request)
    return redirect('user_login')

@login_required
def dashboard_redirect(request):
    """ Redirect user based on role """
    if request.user.role == 'recruiter':
        return redirect('recruiter_dashboard')
    else:
        return redirect('applicant_dashboard')
