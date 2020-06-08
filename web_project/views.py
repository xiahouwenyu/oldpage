from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
import datetime

def hello(request):
    now = datetime.datetime.now()
    html = "<html><body>Hello world.It is now %s.</body></html>" %now
    return HttpResponse(html)

def runoob(request):
    a = ["1", "2", "3"]
    return render(request, 'runoob.html', {'a': a})

def main(request):
    now = datetime.datetime.now()
    bb = get_template('mod.html')
    htt = bb.render(
            {'person_name':"shenhuafei", 'company':'Ynnan University', 'ship_date':now, 
            'item_list':[1,2,3], 'ordered_warranty':'1'})
    return HttpResponse(htt)

def kong(request):
    return render(request, 'index.html')