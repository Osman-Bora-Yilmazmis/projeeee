from autoslug import AutoSlugField
from django.shortcuts import render, redirect
from blog.forms import HijyenForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def hijyen_form(request):
    if request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")
    
    slug = AutoSlugField(populate_from = 'baslik', unique=True, null=True)
    
    form = HijyenForm()
    if request.method == "POST":
        form = HijyenForm(request.POST)
        if form.is_valid():
            hijyen = form.save(commit=False)
            hijyen.form_gonderen = request.user
            form.save()
            return redirect('formlarim')
    context = {
        'form' : form
    }
    return render(request, 'pages/hijyen_form.html', context=context)
