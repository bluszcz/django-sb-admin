from django.shortcuts import render


def start(request):
    """Start page with a documentation.
    """
    return render(request, "django_sb_admin/start.html")