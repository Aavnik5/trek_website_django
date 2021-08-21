from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *
from Accounts.models import *
from core.model import *

# Create your views here.
def home(request):
    try:
        treckcat_obj = trekcategory.objects.all()
        treck_obj = Treck.objects.all()
        context = {'trekcat':treckcat_obj,'treck':treck_obj}
    except Exception as e:
        print(e)    
    return render(request, 'Home.html',context)

def choosetreck(request):
    category = request.GET.get('category')
    treckcat_obj = trekcategory.objects.all()
    choose_obj = Treck.objects.filter(treckcat__category_name=category)
    context = {'trekcat':treckcat_obj,'choose_obj':choose_obj}
     


    return render(request, 'choosetrek.html',context)

def treck(request):
    
    Trakid_obj = request.GET.get('tid')
 
    print("@@@@@@@@@@@@@")
    print(Trakid_obj)
    treckcat_obj = trekcategory.objects.all()
  
    choose_obj = Treck.objects.filter(id=Trakid_obj)
    Itinerary_obj = Itinerary.objects.filter(treck=Trakid_obj)
    trckimage_obj = Treck_Image.objects.filter(treckimg__id=Trakid_obj)
    rvies = review.objects.filter(treckreview=Trakid_obj )
    if request.method == 'POST':
        choose_objs = Treck.objects.filter(id=Trakid_obj).first()    
        reviewes = request.POST.get('write_revi')
        rew_number = request.POST.get('renumbaer')
        rev_obj = review.objects.create(
                    ureview=request.user.usersignup,
                    treckreview = choose_objs,
            
                    reviews = reviewes,
                    review_number=rew_number
                )
           
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))     




    context = {'trekcat':treckcat_obj,'choose_obj':choose_obj,'trck_img':trckimage_obj,'iter_obj':Itinerary_obj,'rvies':rvies}
     
    print(rvies)

    return render(request, 'trecksdetail.html',context)


def contactus(request):
    treckcat_obj = trekcategory.objects.all()
       
    context = {'trekcat':treckcat_obj}
    return render(request, 'contactus.html',context)
def aboutus(request):
    treckcat_obj = trekcategory.objects.all()
       
    context = {'trekcat':treckcat_obj}
    return render(request, 'aboutus.html',context)
def booktreck(request):
    Trakid_obj = request.GET.get('tid')
    treck_obj = Treck.objects.all()
    treckcat_obj = trekcategory.objects.all()
    if request.method == 'POST':
        choose_objs = Treck.objects.filter(id=Trakid_obj).first() 
      
        booknames = request.POST.get('Name')
        bookemails = request.POST.get('Email')
        booknumbesr = request.POST.get('Phone_Number')
        bookaddresss = request.POST.get('Message')
        booknotess = request.POST.get('Note')
        book_obj = Boodtreck.objects.create(
                    userbookid=request.user.usersignup,
                    treckid = choose_objs,
            
                    bookname = booknames,
                    bookemail=bookemails,
                    booknumber=booknumbesr,
                    bookaddress=bookaddresss,
                    booknotes=booknotess,
                )
           
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
       
    context = {'trekcat':treckcat_obj,'treck':treck_obj}
    return render(request, 'booktreck.html',context)