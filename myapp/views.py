



from django.shortcuts import render
from .models import Experience, Project, Certification

def home(request):

    context = {
        'experiences': Experience.objects.all().order_by('-id'), # Latest first
        'projects': Project.objects.all(),
        'certifications': Certification.objects.all(),
    }
    return render(request, 'index.html', context)


from django.shortcuts import render, redirect
from .models import Experience
from django.contrib import messages


def add_experience(request):
    if request.method == "POST":
        # Extracting data from the POST request
        duration = request.POST.get('duration')
        role = request.POST.get('role')
        company = request.POST.get('company')
        stack = request.POST.get('stack')

        # Creating and saving the new Experience object
        new_experience = Experience(
            duration=duration,
            role=role,
            company=company,
            stack=stack
        )
        new_experience.save()

        # Optional: Add a success message
        messages.success(request, "Experience added successfully!")

        # Redirecting to the portfolio home page
        return redirect('home/')

        # If request is GET, just render the form page
    return render(request, 'add_experince.html')


from django.shortcuts import render, redirect
from .models import Project
from django.contrib import messages


def add_project(request):
    if request.method == "POST":
        # Retrieving data from the form
        title = request.POST.get('title')
        features = request.POST.get('features')
        stack = request.POST.get('stack')
        github_link = request.POST.get('github_link')

        # Saving to the Project table
        Project.objects.create(
            title=title,
            features=features,
            stack=stack,
            github_link=github_link
        )

        messages.success(request, "Project deployed to portfolio!")
        return redirect('home/')  # Redirect to your main portfolio page

    return render(request, 'add_project.html')


from django.shortcuts import render, redirect
from .models import Certification
from django.contrib import messages


def add_certificate(request):
    if request.method == "POST":
        # Extracting data from the POST request
        title = request.POST.get('title')
        authority = request.POST.get('authority')

        # Creating and saving the new Certification object
        Certification.objects.create(
            title=title,
            authority=authority
        )

        messages.success(request, "Certification added to your profile!")
        return redirect('home/')

    return render(request, 'add_certificate.html')

from django.shortcuts import render, redirect
from .models import Experience, Project, Certification
from django.contrib.auth.decorators import login_required


def admin_dashboard(request):
    # Fetching all data for the tables
    experiences = Experience.objects.all().order_by('-id')
    projects = Project.objects.all().order_by('-id')
    certifications = Certification.objects.all().order_by('-id')

    # Stats for the dashboard cards
    context = {
        'experiences': experiences,
        'projects': projects,
        'certifications': certifications,
        'exp_count': experiences.count(),
        'proj_count': projects.count(),
        'cert_count': certifications.count(),
    }
    return render(request, 'dashboard.html', context)