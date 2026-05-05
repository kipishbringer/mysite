from django.shortcuts import render
from config.settings import BASE_DIR

def index(request):
    return render(request, f"{BASE_DIR}/main/templates/index.html")
