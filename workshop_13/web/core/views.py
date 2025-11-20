from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from core.models import Product

# Create your views here.
def home_view(request):
    return render(
        request, 
        "home.html",
        {
            "products": Product.objects.all()[:100].order_by("-name")
        }
    )


class HomeView(ListView):
    model = Product
    paginate_by = 1
    template_name = "home.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product.html"
    