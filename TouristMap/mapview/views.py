from django.shortcuts import render
import pg8000
from django.core.cache import cache
from service.models import ServiceImage
context = {}
def index(request):
    obj = ServiceImage.objects.all()
    context['obj'] = obj
    # conn = pg8000.connect(database="tourist_map", user="postgres",password="postgres")
    # cursor = conn.cursor()
    # cursor.execute("Select * from service")
    # results = cursor.fetchall()
    # context['service'] = results
    # for item in list(results):
    #     print(item)
    return render(request, 'map/index3.html',context)
def routing(request):
    return render(request,'Routing.html',context)