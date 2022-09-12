from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import View

from .forms import StockForm
from .models import Stock

# Create your views here.
class Homepage(View):
    template_name = "stock/homepage.html"
    model = Stock.objects.all()


    def get(self, request, *args, **kwargs):
        context = {"stock" : self.model}
        return render(request, self.template_name, context)


class AddForm(FormView):
    template_name = "stock/add_form.html"
    form_class = StockForm
    model = Stock
    #
    def get(self, request, *args, **kwargs):
        form = self.form_class(initial = self.initial)
        context = {"form" : form}
        return render(request, self.template_name, context)


    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
        else:
            form
        context = {"form" : form}
        return render(request, self.template_name, context)
