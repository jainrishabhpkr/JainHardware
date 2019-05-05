
from django.shortcuts import render, redirect
from accounts.forms import ContactForm, LoginForm , RegisterForm , GuestForm
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth import logout
from django.utils.http import is_safe_url
from accounts.models import GuestEmail


# Create your views here.




def login_page(request):
    form = LoginForm()
    print("User logged in:")
    print("lginviewof carts runned")
    print(request.user.is_authenticated())
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    print(request.method)
    if request.method=='POST':
        form = LoginForm(request.POST)
        print("17")
        if form.is_valid():
            print("18")
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(request.user.is_authenticated())
            if user is not None:
                login(request,user)
                print(request.user.is_authenticated())
                if is_safe_url(redirect_path, request.get_host()):
                    print("apple")
                    print(redirect_path)
                    return redirect(redirect_path)
                else:
                    return redirect("/home/")

                # form = LoginForm()

            else:
                print("error")
    mydict={'form':form}
    return render(request,"accounts/login.html",context=mydict)


User = get_user_model()
def register_page(request):
    form = RegisterForm()
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            new_user = User.objects.create_user(username, email, password)
            print(new_user)
    mydict={'form':form}
    return render(request,"accounts/register.html",context=mydict)


def logout_view(request):
    logout(request)
    return render(request,'accounts/logout.html')
    # Redirect to a success page.



def guest_register_view(request):
    form = GuestForm()
    print(" guest User logged in:")
    print(request.user.is_authenticated())
    next_ = request.GET.get('next')
    next_post = request.POST.get('next')
    redirect_path = next_ or next_post or None
    if request.method=='POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            email = form.cleaned_data.get('email')
            print(email)
            new_guest_email = GuestEmail.objects.create(email = email)
            request.session['guest_email_id'] = new_guest_email.id

            if is_safe_url(redirect_path, request.get_host()):
                print("john cena")
                print(redirect_path)
                return redirect(redirect_path)
            else:
                return redirect("carts:checkout")

    mydict={'form':form}
    return redirect("carts:checkout")
