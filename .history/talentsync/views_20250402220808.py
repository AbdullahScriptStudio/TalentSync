from django.shortcuts import render

def custom_404(request, exception):
    return render(request, 'recruiter/error.html', {'status_code': 404}, status=404)

def custom_500(request):
    return render(request, 'recruiter/error.html', {'status_code': 500}, status=500)
