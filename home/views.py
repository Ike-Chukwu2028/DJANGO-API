from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Product
# Create your views here.


class Homepageview(TemplateView):
    template_name= 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        return context
    
class Postdetailview(DetailView):
    template_name= 'detail.html'
    model = Product
