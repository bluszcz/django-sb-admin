from django.shortcuts import render


def start(request):
    """Start page with a documentation.
    """
    return render(
        request,
        "django_sb_admin/start.html",
        {
            "nav_active": "start"
        }
    )

def login(request):
    """Start page with a documentation.
    """
    return render(
        request,
        "django_sb_admin/login.html"
    )

def dashboard(request):
    """Dashboard page.
    """
    return render(
        request,
        "django_sb_admin/sb_admin_dashboard.html",
        {
            "nav_active": "dashboard"
        }
    )

def charts(request):
    """Charts page.
    """
    return render(request, "django_sb_admin/sb_admin_charts.html",
                  {"nav_active":"charts"})
def tables(request):
    """Tables page.
    """
    return render(request, "django_sb_admin/sb_admin_tables.html",
                  {"nav_active":"tables"})
def forms(request):
    """Forms page.
    """
    return render(request, "django_sb_admin/sb_admin_forms.html",
                  {"nav_active":"forms"})
def bootstrap_elements(request):
    """Bootstrap elements page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_elements.html",
                  {"nav_active":"bootstrap_elements"})
def bootstrap_grid(request):
    """Bootstrap grid page.
    """
    return render(request, "django_sb_admin/sb_admin_bootstrap_grid.html",
                  {"nav_active":"bootstrap_grid"})
def dropdown(request):
    """Dropdown  page.
    """
    return render(request, "django_sb_admin/sb_admin_dropdown.html",
                  {"nav_active":"dropdown"})
def rtl_dashboard(request):
    """RTL Dashboard page.
    """
    return render(request, "django_sb_admin/sb_admin_rtl_dashboard.html",
                  {"nav_active":"rtl_dashboard"})

def blank(request):
    """Blank page.
    """
    return render(request, "django_sb_admin/sb_admin_blank.html",
                  {"nav_active":"blank"})
