from django.shortcuts import get_object_or_404, render

from .models import Description, Driver

def driver_list(request):
	drivers = Driver.objects.all()
	#drivers = Driver.objects.prefetch_related('descriptions').all()
	return render(
		request, 
		'drivers/driver_list.html', 
		{'drivers': drivers},
	)