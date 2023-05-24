from django.shortcuts import render, redirect
from blog.forms import TasimaForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

@login_required
def tasima_form(request):

    if request.user.is_staff:
        return HttpResponseForbidden("Bu sayfaya erişmek için yetkiniz yok.")        
    form = TasimaForm()
    if request.method == "POST":
        form = TasimaForm(request.POST)
        if form.is_valid():
            tasima = form.save(commit=False)
            tasima.form_gonderen = request.user
            form.save()
            return redirect('formlarim')
    context = {
        'form' : form
    }
    return render(request, 'pages/tasima_form.html', context=context)

