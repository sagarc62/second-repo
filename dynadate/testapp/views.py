from django.shortcuts import render
import datetime
# Create your views here.
def wish(request):
    date=datetime.datetime.now()
    name='sagar'
    h=int(date.strftime('%H'))
    if h<12:
        msg='Good morning'
    elif h<16:
        msg='Good afternoon'
    elif h<21:
        msg='Good evening'
    else:
        msg='Good night'
    my_dict={'date':date,'name':name,'msg':msg}

    return render(request,'testapp/base.html',context=my_dict)
