from datetime import date
from dateutil.relativedelta import relativedelta
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Application

@login_required
def applicant_dashboard(request):
    user = request.user

    # Ensure only applicants access this page
    if user.role != "applicant":
        messages.error(request, "Unauthorized access.")
        return redirect("job_list")

    applications = Application.objects.filter(applicant_email=user.email)
    total_applications = applications.count()

    # Job Application Trend (Last 6 Months)
    months = []
    application_counts = []
    today = date.today()

    for i in range(5, -1, -1):
        month_date = today.replace(day=1) - relativedelta(months=i)
        months.append(month_date.strftime("%b"))  # Short month name
        count = applications.filter(
            applied_at__year=month_date.year, applied_at__month=month_date.month
        ).count()
        application_counts.append(count)

    context = {
        "applicant_name": user.first_name or user.username,
        "profile_picture": user.profile_pic.url if hasattr(user, "profile_pic") and user.profile_pic else "/static/images/default-profile.png",
        "total_applications": total_applications,
        "recent_applications": applications.order_by("-applied_at")[:5],
        "months": months,
        "application_counts": application_counts,
    }

    return render(request, "applicant/applicant_dashboard.html", context)
