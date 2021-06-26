from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView,  DeleteView,CreateView,UpdateView, FormView
from .models import Customer, Product, Order
from .foms import CreateCustomerForm, CreateOrderForm, CreateProductForm, Registerform
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login

class LoginPageView(LoginView):
    fields = '__all__'
    redirect_authenticated_user = True
    template_name = 'dash/login_view.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:homepage')

class RegisterPageView(FormView):
    form_class = Registerform
    redirect_authenticated_user = True
    template_name = 'dash/register_view.html'
    success_url = reverse_lazy('dashboard:homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPageView, self).form_valid(form)

    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('dashboard:homepage')
        return super(RegisterPageView, self).get(*args,**kwargs)


class AllCustomersView(ListView):
    model = Customer
    template_name = 'dash/allcustomers.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super(AllCustomersView, self).get_context_data(**kwargs)
        context['customer'] = context['customer'].filter(admin_user=self.request.user)
        context['custo_count'] = context['customer'].all().count()
        return context

class AllOrdersView(ListView):
    model = Order
    template_name = 'dash/allorders.html'
    context_object_name = 'order'

    def get_context_data(self, **kwargs):
        context = super(AllOrdersView, self).get_context_data(**kwargs)
        context['order'] = Order.objects.filter(admin_user=self.request.user).order_by('-date')
        context['order_count'] =context['order'].all().count()
        return context


class DashBoardView(ListView):
    model = Customer
    template_name = 'dash/homepage.html'
    context_object_name = 'customer'

    def get_context_data(self, **kwargs):
        context = super(DashBoardView, self).get_context_data(**kwargs)
        context['customer'] = context['customer'].filter(admin_user=self.request.user)[0:4]
        context['order'] = Order.objects.filter(admin_user=self.request.user).order_by('-date')[0:5]
        context['count_delivered'] = Order.objects.filter(admin_user=self.request.user,status='delivered').count()
        context['count_total'] = Order.objects.filter(admin_user=self.request.user).count()
        context['count_pending'] = Order.objects.filter(admin_user=self.request.user,status='pending').count()
        return context



class ProductsView(ListView):
    model = Product
    template_name = 'dash/productpage.html'
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        context['products'] = Product.objects.filter(admin_user=self.request.user)
        return context

class CustomerDetailViewTrial(DetailView):
    model = Customer
    template_name = 'dash/customerspagetrial.html'
    context_object_name = 'customer'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'dash/customerspage.html'
    context_object_name = 'customer'


    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        context['order'] = Order.objects.filter(customer=context['customer'])
        context['cust_count'] = context['order'].count()
        return context


class CustomerCreateView(CreateView):
    form_class = CreateCustomerForm
    template_name = 'dash/customercreate.html'
    success_url = reverse_lazy('dashboard:homepage')

    def form_valid(self, form):
        form.instance.admin_user = self.request.user
        return super(CustomerCreateView,self).form_valid(form)


class OrderCreateView(CreateView):
    form_class = CreateOrderForm
    template_name = 'dash/ordercreate.html'
    success_url = reverse_lazy('dashboard:homepage')

    def form_valid(self, form):
        form.instance.admin_user = self.request.user
        return super(OrderCreateView,self).form_valid(form)

class ProductCreateView(CreateView):
    form_class = CreateProductForm
    template_name = 'dash/productcreate.html'
    success_url = reverse_lazy('dashboard:productpage')
    def form_valid(self, form):
        form.instance.admin_user = self.request.user
        return super(ProductCreateView,self).form_valid(form)


class UpdateCustomer(UpdateView):
    model = Customer
    template_name = 'dash/updatecustomer.html'
    fields = ('name', 'email', 'phone')
    success_url = reverse_lazy('dashboard:homepage')

class DeleteCustomer(DeleteView):
    model = Customer
    template_name = 'dash/deletecustomer.html'
    success_url = reverse_lazy('dashboard:homepage')


class UpdateOrder(UpdateView):
    model = Order
    template_name = 'dash/updateorder.html'
    fields = ('customer','product', 'status')
    success_url = reverse_lazy('dashboard:homepage')

class DeleteOrder(DeleteView):
    model = Order
    template_name = 'dash/deleteorder.html'
    success_url = reverse_lazy('dashboard:homepage')




class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name','category','price')
    template_name = 'dash/productupdate.html'
    success_url = reverse_lazy('dashboard:productpage')


class DeleteProductView(DeleteView):
    model = Product
    template_name = 'dash/deleteproduct.html'
    success_url = reverse_lazy('dashboard:productpage')



