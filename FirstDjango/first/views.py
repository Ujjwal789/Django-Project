from django.shortcuts import render
from .forms import chaivarityForm
from .models import chaivarity
from django.shortcuts import get_object_or_404
from .models import chaivarity, store
# Create your views here.
def first(request):
    chais = chaivarity.objects.all()
    return render(request, 'first/all_first.html',{'chais':chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(chaivarity, pk=chai_id)
    return render(request, 'first/chai_details.html', {'chai':chai})

def store_view(request):
    stores = None

    if request.method == 'POST':
        form = chaivarityForm(request.POST)
        if form.is_valid():
            chai_variety = form.cleaned_data['chai_variety']
            stores = store.objects.filter(chaivarity=chai_variety)
    else:
        form = chaivarityForm()

    return render(request, 'chai_store.html', {
        'stores': stores,
        'form': form
    })
