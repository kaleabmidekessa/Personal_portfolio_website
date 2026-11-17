from django.shortcuts import render

from .models import About,Experience,Project, Skill

def home(request):
    abouts = About.objects.first()
    experiences = Experience.objects.all().order_by('-start_date')
    projects = Project.objects.all()
    skil = Skill.objects.all()

    context = {
        'abouts': abouts,
        'experiences': experiences,
        'projects': projects,
        'skil': skil
    }

    return render(request, 'resume/index.html', context)



