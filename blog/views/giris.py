from blog.models import SunCalisanModel, İdariCalisanModel
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login

class CustomLoginView(LoginView):
    def dispatch(self, request, *args, **kwargs): 
        if self.request.user.is_authenticated: # Kullanıcı oturum açmış durumdayken birdaha login olmaması için
            return redirect('liste')  
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # Giriş işlemi başarılı olduğunda çalışacak kodlar
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            if self.request.user.is_staff:
                return redirect('liste')
            if not self.request.user.is_staff:
                return redirect('formlarim')
        return redirect('giris')
