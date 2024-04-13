from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('admin/dashboard', login_required(views.dashboard, login_url='login'), name='dashboard'),
    # add urls 
    path('admin/dashboard/addpharmacy', login_required(views.AddPharmacy.as_view(), login_url='login'), name='addPharmacy'),
    path('admin/dashboard/adddrug', login_required(views.AddDrug.as_view(), login_url='login'), name='addDrug'),

    # manage urls 
    path('admin/dashboard/managedrug', login_required(views.ManageDrug.as_view(), login_url='login'), name='manageDrug'),
    path('admin/dashboard/managepharmacy', login_required(views.ManagePharmacy.as_view(), login_url='login'), name='managePharmacy'),

    # delete urls
    path('admin/dashboard/pharmacy/delete/<int:pk>', login_required(views.DeletePharmacy.as_view(), login_url='login'), name='deletePharmacy'),
    path('admin/dashboard/drug/delete/<int:pk>', login_required(views.DeleteDrug.as_view(), login_url='login'), name='deleteDrug'),

    # update urls
    path('admin/dashboard/pharmacy/update/<int:pk>', login_required(views.UpdatePharmacy.as_view(), login_url='login'), name='updatePharmacy'),
    path('admin/dashboard/drug/update/<int:pk>', login_required(views.UpdateDrug.as_view(), login_url='login'), name='updateDrug'),

    # display urls
    path('admin/dashboard/pharmacy/view/<int:pk>', login_required(views.PharmacyDetail.as_view(), login_url='login'), name='pharmDetail'),

    path('admin/dashboard/drug/view/<int:pk>', login_required(views.DrugDetail.as_view(), login_url='login'), name='drugDetail'),

    # admin urls
    path('admin/', views.loginPage, name='login'),
    path('admin/logout', views.logoutPage, name='logout'),
    path('', views.LandingPage.as_view(), name='landing'),

    #individual client's urls
    path('pharmacy/', views.pharmacyPage, name='pharmPage'),
    path('pharmacy/<int:pk>', views.pharmacyPagebyId, name='pharmPageId'),
]
