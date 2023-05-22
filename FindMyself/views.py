from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main_view(request):
    user = request.user
    context = {
        'user': user,

    }
    return render(request, 'main/main.html', {})