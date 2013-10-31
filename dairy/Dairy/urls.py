from django.conf.urls import patterns,include,url


urlpatterns=patterns('',
	url(r'^farmers/$','Dairy.views.farmers'),
        url(r'^farmer_details/$','Dairy.views.farmer_details'),
 	url(r'^milk_details/$','Dairy.views.milk_details'),	
	url(r'^animal_details/$','Dairy.views.animal_details'),	
	url(r'all/$', 'Dairy.views.farmer'),
       # url(r'^get/(?P<farmer_id>\d+)/$', 'Dairy.views.farmer1'),
	#url(r'all1/$', 'Dairy.views.animal'),
	#url(r'sunny/$', 'Dairy.views.farmer1'),
        #url(r'^get1/(?P<farmer_id>\d+)/$', 'Dairy.views.farmer11'),
	#url(r'create/$', 'Dairy.views.create'),

)
