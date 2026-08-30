from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Invoice
from .forms import InvoiceForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render

def show_invoices(request):
    
    data = {
        'all_invoices':[
            {'number':1,'customer_name':'Rahul','amoint':100},
            {'number':2,'customer_name':'Ramesh','amoint':200},
            {'number':3,'customer_name':'Suresh','amoint':300},
            {'number':4,'customer_name':'Mahesh','amoint':400},
            {'number':5,'customer_name':'Naresh','amoint':500},
        ]
    }
    

    return render(request, 'invoices/cust_name.html', data)



def add_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all-invoices')
    else:
        form = InvoiceForm()
    
    data = {
        'form':form
    }
    return render(request, 'invoices/add_invoice.html', data)


class HomePageView(TemplateView):
    template_name = 'invoices/home.html'


class InvoiceListView(ListView):
    model = Invoice
    template_name = 'invoices/invoice_list.html'
    context_object_name = 'all_invoices'


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = 'invoices/invoice_detail.html'
    context_object_name = 'invoice'


class InvoiceCreateView(CreateView):
    model = Invoice
    fields = ['customer_name', 'invoice_number', 'amount', 'is_paid']
    template_name = 'invoices/invoice_form.html'
    success_url = '/invoice/'


class InvoiceUpdateView(UpdateView):
    model = Invoice
    fields = ['customer_name', 'invoice_number', 'amount', 'is_paid']
    template_name = 'invoices/invoice_form.html'
    success_url = '/invoice/'


class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = 'invoices/invoice_confirm_delete.html'
    success_url = '/invoice/'