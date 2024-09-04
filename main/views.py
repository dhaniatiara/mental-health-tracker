from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165881',
        'name': 'Dhania Tiaraputri Herdiani',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
