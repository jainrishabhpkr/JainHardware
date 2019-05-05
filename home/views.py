


from django.shortcuts import render, redirect
from accounts.forms import ContactForm
from django.contrib.auth import authenticate, login, get_user_model

# Create your views here.


def homeview(request):
    apple='my name is khan'
    mydict={'apple':apple}
    # print(request.session.get('first_name','unknown'))
    if request.user.is_authenticated():
        mydict['premium']='yeahhhhhhhhhhhh'
    return render(request,'home/home.html',context=mydict)




def contactview(request):
    apple='my name is khan'
    form = ContactForm()
    mydict={'apple':apple, 'form':form}
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("Form validation successs")
            print(form.cleaned_data)
        # print(request.POST.get('fullname'))
        # print(request.POST.get('email'))
        # print(request.POST.get('content'))

    return render(request,'home/contact.html',context=mydict)
