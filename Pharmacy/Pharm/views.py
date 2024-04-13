from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, TemplateView
from .models import Drug, Pharmacy
from django.views.generic.detail import DetailView
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    pharmacy = Pharmacy.objects.count()
    template_name = "Pharm/admin/dashboard.html"
    return render(request, template_name , {'pharmacy': pharmacy})

class ManagePharmacy(TemplateView):
    template_name = 'Pharm/admin/products/product.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ManagePharmacy, self).get_context_data(**kwargs)
        context['products'] = Pharmacy.objects.all()
        return context

class ManageDrug(TemplateView):
    template_name = 'Pharm/admin/drug/product.html'
    def get_context_data(self, *args, **kwargs):
        context = super(ManageDrug, self).get_context_data(**kwargs)
        context['products'] = Drug.objects.all()
        return context

class AddPharmacy(CreateView):
    template_name = 'Pharm/admin/products/food_form.html'
    model = Pharmacy
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        context = super(AddPharmacy, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Pharmacy Was Added Successfully.")
        return super(AddPharmacy, self).form_valid(form)
    def form_invalid(self, form):
        messages.success(self.request, "An error occured while adding the drug!")
        return super(AddPharmacy, self).form_invalid(form)

class AddDrug(CreateView):
    template_name = 'Pharm/admin/drug/food_form.html'
    model = Drug
    fields = '__all__'
    def get_context_data(self, *args, **kwargs):
        context = super(AddDrug, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Drug Was Added Successfully.")
        return super(AddDrug, self).form_valid(form)


class DeletePharmacy(DeleteView):
    model = Pharmacy
    template_name = 'Pharm/admin/products/delete_form.html'
    success_url =  reverse_lazy('managePharmacy')
    def get_context_data(self, *args, **kwargs):
        context = super(DeletePharmacy, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Pharmacy Deleted Successfully.")
        return super(DeletePharmacy, self).form_valid(form)

class DeleteDrug(DeleteView):
    model = Drug
    template_name = 'Pharm/admin/drug/delete_form.html'
    success_url =  reverse_lazy('manageDrug')
    def get_context_data(self, *args, **kwargs):
        context = super(DeleteDrug, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Drug Deleted Successfully.")
        return super(DeleteDrug, self).form_valid(form)

class UpdatePharmacy(UpdateView):
    model = Pharmacy
    template_name = 'Pharm/admin/products/update_form.html'
    fields = '__all__'
    success_url =  reverse_lazy('managePharmacy')
    def get_context_data(self, *args, **kwargs):
        context = super(UpdatePharmacy, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Pharmacy Updated Successfully.")
        return super(UpdatePharmacy, self).form_valid(form)

class UpdateDrug(UpdateView):
    model = Drug
    template_name = 'Pharm/admin/drug/update_form.html'
    fields = '__all__'
    success_url =  reverse_lazy('manageDrug')
    def get_context_data(self, *args, **kwargs):
        context = super(UpdateDrug, self).get_context_data(**kwargs)
        return context
    def form_valid(self, form):
        messages.success(self.request, "Drug Updated Successfully.")
        return super(UpdateDrug, self).form_valid(form)

class PharmacyDetail(DetailView):
    model = Pharmacy
    template_name = 'Pharm/admin/products/view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class DrugDetail(DetailView):
    model = Drug
    template_name = 'Pharm/admin/drug/view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def loginPage(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.info(request, "Incorrect Login details")
    return render(request, "Pharm/login.html")


def logoutPage(request):
    logout(request)
    return redirect("login")


class LandingPage(TemplateView):
    template_name = 'Pharm/landingPage/index.html'
    def get_context_data(self, *args, **kwargs):
        context = super(LandingPage, self).get_context_data(**kwargs)
        context['pharmacy'] = Pharmacy.objects.all()
        return context

def pharmacyPage(request):
    model = Pharmacy
    template_name = 'Pharm/pharmacy/index.html'
    if request.method == 'POST':
        pharmId = request.POST['pharmacy']
        pharmacy = Pharmacy.objects.get(id=pharmId)
        drugs = pharmacy.drugs
        return render(request, template_name, {'pharmacy': pharmacy, 'drugs': drugs})
    else:
        return render(request, template_name)

def pharmacyPagebyId(request, pk):
    template_name = 'Pharm/pharmacy/index.html'
    pharmacy = Pharmacy.objects.get(id=pk)
    drugs = pharmacy.drugs
    
    return render(request, template_name, {'pharmacy': pharmacy, 'drugs': drugs})