from django.shortcuts import render
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


class AddForm(View):
    template_name = "stock/homepage.html"
    form = StockForm
    model = Stock()
    #
    def get(self, request, *args, **kwargs):
        form = StockForm(request.POST or None)
        context = {"form" : form}
        return render(request, self.template_name, context)



    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = StockForm(request.POST or None)
            if form.is_valid():
                form.save()
            else:
                form
            context = {"form" : form}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, context)
