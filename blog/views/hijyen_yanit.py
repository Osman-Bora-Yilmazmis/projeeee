from autoslug import AutoSlugField
from django.shortcuts import render, redirect
from blog.forms import HijyenYanit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def hijyen_yanit(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")
    
    
    hijyen_yanit = HijyenYanit()
    if request.method == "POST":
        hijyen_yanit = HijyenYanit(request.POST)
        if hijyen_yanit.is_valid():
            hijyen_yanit.save()
            return redirect('liste')
    context = {
        'hijyen_yanit' : hijyen_yanit
    }
    return render(request, 'pages/hijyen_yanit.html', context=context)
