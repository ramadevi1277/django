# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from Dairy.models import Farmer
from forms import FarmerForm
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf



def hello(request):
	#import pdb
        #pdb.set_trace()
        div_object="<div><ul>%s</ul></div>"
        a=request.GET
	get_li="<li>%s</li>"
        list_li=[]
        for each in a:
		get_object=get_li %a[each]
 		list_li.append(get_object)
       
	return HttpResponse(div_object%"".join(list_li))
	#return render_to_response('farmer1.html'{'details':request.GET})
def farmers(request):
	return render_to_response('base.html')
def farmer_details(request):
	return render_to_response('farmer_details.html')
def milk_details(request):
	return render_to_response('milk_Details.html')
def animal_details(request):
	return render_to_response('animal_details.html')


