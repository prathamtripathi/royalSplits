from django.shortcuts import render,redirect,get_object_or_404
from .models import About,Coupon,Product,Order,OrderItem, Blog,Comment,AuthorAbout,Job,JobApplication,AboutUs,New,ContactU,Customer,WholeSale,Address,Payment
from .forms import CommentForm,JobForm,CouponForm,CheckoutForm,ColorForm,ProfileForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from django.conf import settings
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponse,JsonResponse  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
import json
from django.contrib.auth import logout as auth_logout, get_user_model
from .utils import cookieCart
def create_ref_code():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=20))

def get_coupon(request, code):
    try:
        coupon = Coupon.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, "This coupon does not exist")
        return redirect('cart')

def home(request):
    about = About.objects
    prod = Product.objects


    context = {'about':about,'prod':prod}
    return render(request, 'home/home_about.html',context)


def cart(request):
    prods = Product.objects
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']

    context = {'items':items,'prods':prods,'order':order,'couponform': CouponForm(),'color':ColorForm() }
    return render(request,'home/cart.html',context)


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST)
        if form.is_valid():
            try:
                customer, created = Customer.objects.get_or_create(user=self.request.user)
                code = form.cleaned_data.get('code')
                order = Order.objects.get(
                    customer=customer,complete=False)
                order.coupon = get_coupon(self.request, code)
                order.save()
                messages.success(self.request, "Successfully added coupon")
                return redirect('cart')
            except ObjectDoesNotExist:
                messages.info(self.request, "You do not have an active order")
                return redirect('cart')

def choose_color(request,id):
    try:
        item= get_object_or_404(Product, id=id)
        form = ColorForm(request.POST)
        order_item = OrderItem.objects.filter(
            product=item)
        
        if form.is_valid():
            color = form.cleaned_data.get('color')
            order_item.all().update(color=color)
            return redirect('cart')

    except ObjectDoesNotExist:
        return render('cart')


def checkout(request):
    form = CheckoutForm()
    if request.user.is_authenticated:
        customer, created = Customer.objects.get_or_create(user=request.user)
        order,created = Order.objects.get_or_create(customer=customer,complete=False)
        items = order.orderitem_set.all()
    else:
        cookieData = cookieCart(request)
        order = cookieData['order']
        items = cookieData['items']


        
    if request.method == 'POST': 
        form = CheckoutForm(request.user)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            address = form.cleaned_data.get('address')
            country = form.cleaned_data.get('country')
            state = form.cleaned_data.get('state')
            zip_code = form.cleaned_data.get('zip_code')
            payment_option = form.cleaned_data.get('payment_option')
            checking = Address(user=request.user,name=name,email=email,address=address,
                country=country,state=state,zip_code=zip_code,payment_option=payment_option)
            checking.save()
            return redirect('checkout')
    context = {'items':items,'order':order,'form':form}
    return render(request,'home/checkout.html',context)


def update_item(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print(action)
    print(productId)
    customer, created = Customer.objects.get_or_create(user=request.user)
    product = Product.objects.get(id=productId)
    order,created = Order.objects.get_or_create(customer=customer,complete=False)
    orderItem,created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':
        orderItem.quantity+=1
    elif action == 'remove':
        orderItem.quantity-=1
    orderItem.save()
    if orderItem.quantity<=0:
        orderItem.delete()
    return JsonResponse('Item was Updated',safe=False)

























# def detail(request,slug):
#     ob_item = get_object_or_404(Product,slug=slug)
#     prods = Product.objects
#     context = {'object':ob_item,'prods':prods}
#     return render(request,'home/description.html',context)


def page_about(request):
    about = get_object_or_404(AboutUs)
    prod = New.objects
    context = {'about':about,'prod':prod}
    return render(request, 'home/page-about-company.html',context)



def profile_setting(request):
    if request.method == 'POST':
        form =ProfileForm(request.POST)
        if form.is_valid():
            fname = form.cleaned_data.get('fname')
            lname=form.cleaned_data.get('lname')   
            location=form.cleaned_data.get('location')
            website=form.cleaned_data.get('website')
            bio=form.cleaned_data.get('bio')
            profile = Customer(
                user=request.user,
                fname=fname,
                lname=lname,
                location=location,
                website=website,
                bio=bio
                )
            profile.update(user=request.user,
                fname=fname,
                lname=lname,
                location=location,
                website=website,
                bio=bio)
            return redirect('profile_setting')
    else:
        form = ProfileForm()
        profile = Customer.objects.get(user = request.user)
        context = {
            'form':form,
            'profile':profile
        }
        return render(request, 'home/page-settings.html',context)






# class ProfileSetting(View):

#     def get(self,*args,**kwargs):
#         form = ProfileForm()
#         profile = Customer.objects.get(user=self.request.user)
#         context = {
#             'form':form,
#             'profile':profile
#         }
#         return render(self.request, 'home/page-settings.html',context)
#     def post(self,*args,**kwargs):
#         form = ProfileForm()    
#         if form.is_valid():
#             fname = form.cleaned_data.get('fname')
#             lname=form.cleaned_data.get('lname')   
#             location=form.cleaned_data.get('location')
#             website=form.cleaned_data.get('website')
#             bio=form.cleaned_data.get('bio')
#             profile = Customer(
#                 user=self.request.user,
#                 fname=fname,
#                 lname=lname,
#                 location=location,
#                 website=website,
#                 bio=bio
#                 )
#             profile.save()
#             return redirect('profile_setting')
#         messages.info(self.request,"We will update your Profile SOON")
#         return redirect('home')




def formpage(request):
    if request.method == 'POST':
        cname= request.POST.get('name')
        Fname= request.POST.get('Fname')
        Lname= request.POST.get('Lname')
        title= request.POST.get('title')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        fax = request.POST.get('fax')
        products= request.POST.get('Products')
        quantity= request.POST.get('Quantity')
        msg= request.POST.get('msg')
        city= request.POST.get('city')
        state= request.POST.get('State')
        zip_code= request.POST.get('zip_code')
        country= request.POST.get('country')
        tax= request.POST.get('tax')
        resell= request.POST.get('resell')
        insta= request.POST.get('insta')
        facebook= request.POST.get('facebook')
        products1= request.POST.get('Products1')
        ms2= request.POST.get('ms2')
        city1= request.POST.get('city1')
        state1= request.POST.get('State1')
        zip1= request.POST.get('zip1')
        country1= request.POST.get('country1')
        name1= request.POST.get('name1')
        phone11= request.POST.get('phone11')
        whole_sale_info = WholeSale(cname=cname,fname=Fname,lname=Lname,ctitle=title,email=email,phnumber=phone,fnum=fax,
            product_choice=products,quantity=quantity,address=msg,city=city,state=state,zip_code=zip_code,country=country,federal_tax_id=tax,
            reseller_lisence=resell,inst_id=insta,fb_id=facebook,shipping_add_field=products1,shipping_add=ms2,shipping_city=city1,
            shipping_state=state1,shipping_zip=zip1,shipping_country=country1,shipping_person_name=name1,shipping_person_num=phone11)
        whole_sale_info.save()
        messages.info(request, "Thanks for submiting the form we will shortly fulfill your order")
        return redirect('formpage')
    else:
        return render(request,'home/formpage.html')
    

def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    phone_no = request.POST.get('phone')
    description = request.POST.get('msg')
    contact_info = ContactU(name=name,email=email,phone_no=phone_no,description=description)
    contact_info.save()
    return render(request,'home/contactus.html')


def tnc(request):
    return render(request,'home/tnc.html')

def page_404(request):
    return render(request,'home/page_404.html')
    
def page_500(request):
    return render(request,'home/page_500.html')

def blog_list(request):
    blogs=Blog.objects
    return render(request,'home/blog_list.html',{'blogs':blogs})

def BlogDetailView(request,_id):
    try:
        data =Blog.objects.get(id=_id)
        comments = Comment.objects.filter(blog = data)
        auth = AuthorAbout.objects.get(id=_id)
    except Blog.DoesNotExist:
        raise Http404('Data does not exist')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(your_name= form.cleaned_data['your_name'],comment_text=form.cleaned_data['comment_text'],blog=data)
            comment.save()
            return redirect(f'/blog_detail/{_id}')
    else:
        form = CommentForm()
        context = {
            'data':data,
            'form':form,
            'comments':comments,
            'auth':auth
        }

    return render(request,'home/blog_article.html',context)
    


def page_career(request):
    job = Job.objects.all
    return render(request,'home/page_career.html',{'job':job})

def jobA(request,id):
    job_data = get_object_or_404(Job,pk=id)
    if request.method == 'POST':
        form = JobForm(request.POST,request.FILES)
        if form.is_valid():
            
            model_instance = JobApplication(full_name=form.cleaned_data['full_name'],email=form.cleaned_data['email'],
                reason=form.cleaned_data['reason'],resume = request.FILES.get('resume'),job_title=job_data)
            model_instance.save()
            messages.info(request, "Thanks for submiting the form we will look at your resume and if you are shortlisted our team will contact you")
            return redirect('page_career')
    else:
        form = JobForm()
        context = {
        'form':form,
        'job_data':job_data}
        return render(request,'home/jobA.html',context)

def maintain(request):
    return render(request,'home/maintain.html')

def findus(request):
    return render(request,'home/findus.html')






def remove_account(request):
    user_pk = request.user.pk
    auth_logout(request)
    User = get_user_model()
    User.objects.filter(pk=user_pk).update(is_active=False)
    return redirect('home')






    