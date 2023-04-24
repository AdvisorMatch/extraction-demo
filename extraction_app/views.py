from django.shortcuts import render, get_object_or_404
from keybert import KeyBERT

# Create your views here.
import requests

from .filters import WorkFilter
from .models import Work, Advisor
from .settings import STUDENT_ID, STUDENT_EMAIIL

kw_model = KeyBERT()


def extract(request):
    """
    Extract data from example source (Projar)
    """
    token_response = requests.post("https://ecourse.cpe.ku.ac.th/projar/api/token/pair", json={
        "username": STUDENT_ID,
        "password": STUDENT_EMAIIL
    }, headers={
        "Content-Type": "application/json"
    })
    token_data = token_response.json()
    access_token = token_data['access']
    for year in range(2556, 2566):
        projects_response = requests.get(f"https://ecourse.cpe.ku.ac.th/projar/api/projects/{year}", headers={
            'Authorization': f"Bearer {access_token}"
        })
        projects = projects_response.json()['projects']
        for project in projects:
            if Work.objects.filter(source_id=project['id']).exists():
                continue
            # Co-advisor is not considered in this demo
            advisor, _ = Advisor.objects.get_or_create(full_name=project['advisor'])
            Work.objects.create(
                source_id=project['id'],
                title=project['title_en'],
                abstract=project['abstract_en'],
                year=project['year'],
                work_type=project['type'],
                raw_keywords=project['keywords'],
                advisor=advisor
            )
    return render(request, 'extraction_app/extract_success.html')


def list_works(request):
    f = WorkFilter(request.GET, queryset=Work.objects.all())
    return render(request, 'extraction_app/list.html', {'filter': f})


def work_detail(request, id):
    work = get_object_or_404(Work, id=id)
    # (keyword, distance)
    keywords = kw_model.extract_keywords(work.abstract)
    return render(request, 'extraction_app/detail.html', {
        'work': work,
        'keywords': keywords
    })
