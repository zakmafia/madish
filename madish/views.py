from django.shortcuts import render, redirect

def home(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        return render(request, 'index.html')