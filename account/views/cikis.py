from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def cikis(request):
    logout(request)
    return redirect('giris') #liste değil log-in sayfası olacak