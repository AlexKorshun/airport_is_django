from django.contrib import admin
from django.urls import path
from airport import views
urlpatterns = [
 path('admin/', admin.site.urls),
 path('', views.flight_list, name='flight_list'),
 path('book/<int:flight_id>/', views.book_flight, name='book_flight'),
]
