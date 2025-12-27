from django.db import models
class Aircraft(models.Model):
 TYPE_CHOICES=[('plane','Самолёт'),('helicopter','Вертолёт')]
 model=models.CharField('Модель',max_length=100)
 aircraft_type=models.CharField('Тип',max_length=20,choices=TYPE_CHOICES)
 seats=models.PositiveIntegerField('Количество мест')
 def __str__(self): return f"{self.model} ({self.get_aircraft_type_display()})"
class Flight(models.Model):
 direction=models.CharField('Направление',max_length=150)
 departure_time=models.DateTimeField('Время вылёта')
 aircraft=models.ForeignKey(Aircraft,on_delete=models.CASCADE)
 price=models.DecimalField('Цена',max_digits=8,decimal_places=2)
 def __str__(self): return f"{self.direction} — {self.departure_time:%d.%m.%Y %H:%M}"
class Booking(models.Model):
 passenger_name=models.CharField('ФИО пассажира',max_length=150)
 flight=models.ForeignKey(Flight,on_delete=models.CASCADE)
 created_at=models.DateTimeField('Дата бронирования',auto_now_add=True)
 def __str__(self): return f"{self.passenger_name} / {self.flight}"
