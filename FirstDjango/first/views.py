from django.shortcuts import render
from .models import chaivarity
from django.shortcuts import get_object_or_404
# Create your views here.
def first(request):
    chais = chaivarity.objects.all()
    return render(request, 'first/all_first.html',{'chais':chais})

def chai_details(request, chai_id):
    chai = get_object_or_404(chaivarity, pk=chai_id)
    return render(request, 'first/chai_details.html', {'chai':chai})