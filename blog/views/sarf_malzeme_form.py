from django.shortcuts import render, redirect
from blog.forms import SarfMalzemeForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
import django.contrib.sessions.middleware
@login_required
def sarf_malzeme_form(request):

    if request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")        
    form = SarfMalzemeForm()
    if request.method == "POST":
        form = SarfMalzemeForm(request.POST)
        if form.is_valid():
            sarf = form.save(commit=False)
            sarf.form_gonderen = request.user
            form.save()
            return redirect('formlarim')
    context = {
        'form' : form
    }
    return render(request, 'pages/sarf_malzeme_form.html', context=context)

