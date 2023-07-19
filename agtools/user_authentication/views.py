from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from user_authentication.forms import LoginForm


class LoginTemplateView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'auth/login.html'

    def get(self, request, message=''):
        form = LoginForm()
        return Response(
            {'form': form, 'error': message},
        )

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/customers/')
        return self.get(request, message='Usuário ou senha incorretos.')


def logout_view(request):
    logout(request)
    return redirect('/')
