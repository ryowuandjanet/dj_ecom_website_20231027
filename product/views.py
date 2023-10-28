from typing import Any, Dict
from django.views import generic

from .models import (
  Category,
  Product,
  Slider
)

class Home(generic.TemplateView):
  template_name = 'home.html'

  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context =  super().get_context_data(**kwargs)
    context.update(
      {
        'featured_categories': Category.objects.filter(featured = True),
        'featured_products': Product.objects.filter(featured = True),
        'sliders': Slider.objects.filter(show=True)
      }
    )
    return context

class ProductDetails(generic.TemplateView):
  template_name = 'product/product-details.html'