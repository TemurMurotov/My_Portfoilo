from django.shortcuts import render
from django.http import JsonResponse
from .models import Project, SocialLink

def home(request):
    context = {
        'projects': Project.objects.all(),
        'social_links': SocialLink.objects.all(),
    }
    return render(request, 'core/home.html', context)
# ===== API VIEWS =====

def api_projects(request):
    projects = Project.objects.all()
    data = []
    for p in projects:
        data.append({
            'id': p.id,
            'title': p.title,
            'description': p.description,
            'tech_stack': p.tech_stack,
            'github_url': p.github_url,
            'live_url': p.live_url,
            'image': p.image.url if p.image else None,
        })
    return JsonResponse({'projects': data})


def api_project_detail(request, project_id):
    try:
        p = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return JsonResponse({'error': 'Loyiha topilmadi'}, status=404)
    data = {
        'id': p.id,
        'title': p.title,
        'description': p.description,
        'tech_stack': p.tech_stack,
        'github_url': p.github_url,
        'live_url': p.live_url,
        'image': p.image.url if p.image else None,
    }
    return JsonResponse(data)


def api_social_links(request):
    links = SocialLink.objects.all()
    data = [{'platform': l.platform, 'url': l.url} for l in links]
    return JsonResponse({'social_links': data})