from django.shortcuts import render, get_object_or_404, redirect
from .models import Region,Pays
from .forms import PaysForm,RegionForm
# Create your views here.

def home(request):
    return render(request, 'monapp/home.html')

 #PAYS
def liste_pays(request):
    pays = Pays.objects.all()
    print("Pays récupérés :", pays)
    return render(request,'monapp/liste_pays.html',{'pays':pays})

def ajouter_pays(request):
    form =  PaysForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("liste_pays")
    return render(request,'monapp/form_pays.html',{'form':form})

def modifier_pays(request,id):
    pays = get_object_or_404(Pays,pk=id)
    form = PaysForm(request.POST or None,instance = pays)
    if form.is_valid():
        form.save()
        return redirect("liste_pays")
    return render(request, 'monapp/form_pays.html',{'form':form})

def supprimer_pays(request,id):
    pays = get_object_or_404(Pays, pk =id)
    pays.delete()
    return redirect("liste_pays")

#REGIONS

def liste_regions(request):
    regions = Region.objects.all()
    return render(request,'monapp/liste_regions.html',{'regions':regions})

def ajouter_region(request):
    form =  RegionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("liste_regions")
    return render(request,'monapp/form_region.html',{'form':form})

def modifier_region(request,id):
    pays = get_object_or_404(Region,pk=id)
    form = RegionForm(request.POST or None,instance = region)
    if form.is_valid():
        form.save()
        return redirect("liste_regions")
    return render(request, 'monapp/form_region.html',{'form':form})

def supprimer_region(request,id):
    region = get_object_or_404(Region, pk =id)
    region.delete()
    return redirect("liste_regions")