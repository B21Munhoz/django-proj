from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from customer.forms import CustomerCreationForm
from customer.models import get_all_customers
from customer.serializers import CustomerSerializer


class CustomerAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    def get(self, request):
        # Retorna todos os clientes
        customers_list = get_all_customers()
        serializer = CustomerSerializer(customers_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Cria um novo cliente
        serializer = CustomerSerializer(data=request.data)
        try:
            if serializer.is_valid(raise_exception=True):
                serializer.save()
            return Response(
                {'detail': 'Success'},
            )
        except Exception as e:
            return Response({'detail': str(e)}, status=400)


class CustomerTemplateView(LoginRequiredMixin, APIView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customer/customers_list.html'

    api_view = CustomerAPIView()

    def get(self, request):
        # Renderiza todos os clientes
        response = self.api_view.get(request)
        customers_dict = {'customers': response.data}
        return Response(customers_dict)


class CustomerFormTemplateView(LoginRequiredMixin, APIView):
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'customer/register_customer.html'

    api_view = CustomerAPIView()

    def get(self, request):
        # Renderiza a Template do Form
        form = CustomerCreationForm()
        return Response(
            {'form': form, 'message': ''},
        )

    def post(self, request, *args, **kwargs):
        response = self.api_view.post(request)
        form = CustomerCreationForm()
        message = ''
        status = response.status_code

        if response.data['detail'] == 'Success':
            message = 'Cliente registrado!'
        elif 'email' in response.data['detail']:
            message = 'Este e-mail já está sendo usado!'
        else:
            message = 'Erro inesperado'

        return Response({'form': form, 'message': message}, status=status)
