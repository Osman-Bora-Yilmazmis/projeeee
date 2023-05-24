from autoslug import AutoSlugField
from django.shortcuts import render, redirect
from blog.forms import TasimaYanit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def tasima_yanit(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")
    
    
    tasima_yanit = TasimaYanit()
    if request.method == "POST":
        tasima_yanit = TasimaYanit(request.POST)
        if tasima_yanit.is_valid():
            tasima_yanit.save()
            return redirect('liste')
    context = {
        'tasima_yanit' : tasima_yanit
    }
    return render(request, 'pages/tasima_yanit.html', context=context)
