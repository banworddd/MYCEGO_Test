from django.shortcuts import render

def files_view(request):
    return render(request, 'web/files.html')
