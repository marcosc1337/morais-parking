from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    template_name = 'register.html'
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegisterForm()
    
    context_to_render = {
        'form': form
    }
    return render(request, template_name, context_to_render)
