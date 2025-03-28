from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Application
from datetime import datetime, timedelta

@login_required
def applicant_dashboard(request):
    user = request.user

    # Ensure only applicants access this page
    if user.role != "applicant":
        return render(request, "error.html", {"message": "Access Denied"})

    applications = Application.objects.filter(applicant_email=user.email)
    total_applications = applications.count()

    # Job Application Trend (Last 6 Months)
    months = [(datetime.now() - timedelta(days=30 * i)).strftime("%b") for i in reversed(range(6))]
    application_counts = [
        applications.filter(applied_at__month=(datetime.now() - timedelta(days=30 * i)).month).count()
        for i in reversed(range(6))
    ]

    context = {
        "applicant_name": user.first_name or user.username,
        "profile_picture": user.profile_pic.url if user.profile_pic else "/static/images/default-profile.png",
        "total_applications": total_applications,
        "recent_applications": applications.order_by("-applied_at")[:5],
        "months": months,
        "application_counts": application_counts,
    }

    return render(request, "applicant_dashboard.html", context)
