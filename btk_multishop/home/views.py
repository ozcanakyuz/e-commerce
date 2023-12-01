from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import logout, authenticate, login

from home.forms import LoginForm, SignUpForm
from home.models import UserProfile, UserProfileForm, ContactFormMessage
from product.models import Product, Category
from order.models import ShopCart


def index(request):
    slider = Product.objects.all() #! Sidebar.html slider içerisinde.
    # urunler = Product.objects.order_by('?')[:8] #! .objects.all()[:8] tane resim seç demek! .objects.order_by('?')[:8] ise random şekilde ayarlar.
    context = {'page': 'home',
               'slider': slider,}
            #    'urunler': urunler}
    return render(request, 'index.html', context)

def shop(request):
    context = {'page': 'shop'}
    return render(request, 'shop.html', context)
def detail(request):
    context = {'page': 'detail'}
    return render(request, 'detail.html', context)
def contact(request):
    context = {'page': 'contact'}
    return render(request, 'contact.html', context)
def checkout(request):
    context = {'page': 'checkout'}
    return render(request, 'checkout.html', context)

#! LOG IN 
def login_view(request):
    # category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['cart_items'] = ShopCart.objects.filter(user_id=user.id).count()
                messages.success(request, "Başarılı şekilde oturum açtınız {}".format(user.username))
                return HttpResponseRedirect('/user/userprofile')
            else:
                messages.warning(request, "Girilen Bilgiler Hatalı Tekrar Deneyiniz {}".format(username))
                return HttpResponseRedirect('/login')
                
    form = LoginForm
    context = {'form': form}
    return render(request, 'login.html', context)

#! LOG OUT 
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')

#! SIGN IN
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save() #completed sign up
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            # Create data in profile table for user
            current_user = request.user
            data=UserProfile()
            data.user_id=current_user.id
            data.image="images/users/user.png"
            data.save()
            # sonradan eklenecek kısım
            messages.success(request, 'Your account has been created!')
            return HttpResponseRedirect('/')
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect('/signup')
            
    form = SignUpForm()
    context = {'form': form}
    return render(request, 'signup_form.html', context)

#! USER PROFILE 
def userProfile_view(request):
    category = Category.objects.all()
    if request.method == 'POST':  # check post
        form = UserProfileForm(request.POST)
        if form.is_valid():
            data = ContactFormMessage()  # create relation with model
            data.name = form.cleaned_data['name']  # get form input data
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()  # save data to table
            messages.success(request, "Your message has ben sent. Thank you for your message.")
            return HttpResponseRedirect('/user_profile')
            
    form = UserProfileForm
    context = {'form': form}
    return render(request, 'userprofile.html', context)