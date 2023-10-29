from typing import Any, Dict
from django.views import generic
from django.core.paginator import (
    PageNotAnInteger,
    EmptyPage,
    InvalidPage,
    Paginator
)

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

class ProductDetails(generic.DetailView):
    model = Product
    template_name = 'product/product-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['related_products'] = self.get_object().related
        return context

class CategoryDetails(generic.DetailView):
    model = Category
    template_name = 'product/category-details.html'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['products'] = self.get_object().products.all()
        return context

class CustomerPaginator:
    def __init__(self,request,queryset,paginted_by) -> None:
        self.paginator = Paginator(queryset,paginted_by)
        self.paginated_by = paginted_by
        self.queryset = queryset
        self.page = request.GET.get('page',1)
    
    def get_queryset(self):
        try:
            queryset = self.paginator.page(self.page)
        except PageNotAnInteger:
            queryset = self.paginator.page(1)
        except EmptyPage:
            queryset = self.paginator.page(1)
        except InvalidPage:
            queryset = self.paginator.page(1)
        return queryset

class ProductList(generic.ListView):
    model = Product
    template_name = 'product/product-list.html'
    context_object_name = 'object_list'
    paginate_by = 5

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context =  super().get_context_data(**kwargs)
        page_obj = CustomerPaginator(self.request, self.get_queryset(),self.paginate_by)
        queryset = page_obj.get_queryset()
        paginator = page_obj.paginator
        context['object_list'] = queryset
        context['paginator'] = paginator
        return context