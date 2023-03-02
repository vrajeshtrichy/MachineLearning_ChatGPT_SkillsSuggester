from django.shortcuts import render
from django.conf import settings
# Create your views here.
from django.http import HttpResponse

import openai

openai.api_key = settings.OPENAI_API_KEY


def index(request):
    result = ''
    question = ''
    if request.method == "POST":
        role = request.POST.get('role')
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(role),
            temperature=0.6,
        )
        question = role
        result = response.choices[0].text
    return render(request, 'suggestSkills/index.html', {'result': result, 'question': question})


def generate_prompt(role):
    return """Suggest three skills for role that is related to data.
                Role: Data Scientist
                Skills: Statistical Analysis, Programming, Machine Learning
                Role: AI Engineer
                Skills: Machine Learning, Programming, Distributed Systems
                Role: {}
                Skills:""".format(role.capitalize())
