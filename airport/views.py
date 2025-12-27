from django.shortcuts import render,redirect,get_object_or_404
from .models import Flight
from .forms import BookingForm
def flight_list(request):
 flights=Flight.objects.all().order_by('departure_time')
 return render(request,'airport/flight_list.html',{'flights':flights})
def book_flight(request,flight_id):
 flight=get_object_or_404(Flight,id=flight_id)
 if request.method=='POST':
  form=BookingForm(request.POST)
  if form.is_valid():
   booking=form.save(commit=False)
   booking.flight=flight
   booking.save()
   return redirect('flight_list')
 else:
  form=BookingForm()
 return render(request,'airport/book_flight.html',{'form':form,'flight':flight})
