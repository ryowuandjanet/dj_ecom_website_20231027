from django.views import generic

class Home(generic.TemplateView):
  template_name = 'home.html'

class ProductDetail(generic.TemplateView):
  template_name = 'product/product-details.html'