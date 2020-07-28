from django.shortcuts import render
from .models import MsgDet

# Create your views here.

def voir(request):
    myobj = MsgDet.objects.get(id=1)
    print(myobj)
    return render(request, 'myinfo.html', {'object': myobj})
