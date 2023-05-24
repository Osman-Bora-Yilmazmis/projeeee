from django.shortcuts import render, redirect
from blog.forms import SarfYanit
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import django.contrib.sessions.middleware

@login_required
def sarf_malzeme_yanit(request):

    if not request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")        
    sarf_yanit = SarfYanit()
    if request.method == "POST":
        sarf_yanit = SarfYanit(request.POST)
        if sarf_yanit.is_valid():
            request.form_gonderen = request.session.get('form_gonderen')
            sarf_yanit.save()
            return redirect('liste')
    context = {
        'sarf_yanit' : sarf_yanit
    }
    return render(request, 'pages/sarf_malzeme_yanit.html', context=context)

