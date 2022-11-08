from django.forms import ModelForm
from blog.models import Products

class ProductModelForm(ModelForm):
    class Meta:
        model = Products
        exclude = []