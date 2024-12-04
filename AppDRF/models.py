from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator,MinValueValidator, MinLengthValidator, MaxLengthValidator

class Base(models.Model):
    created_at= models.DateTimeField(default=now)
    updated_at= models.DateTimeField(default=now)
    is_active= models.BooleanField(default=True)
    
    class Meta:
        db_table='Base'
        abstract=True

class Country(Base):
    country_name=models.CharField(max_length=20)
    code=models.IntegerField(validators= [MinValueValidator(0)])
    short_name=models.CharField(validators=[MinLengthValidator(3)],max_length=10)
    flag=models.ImageField(upload_to='image/')

    class Meta:
        db_table='Country'
    def __str__(self):
        return self.country_name

class State(Base):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='state')
    state_name=models.CharField(max_length=20)
    short_name=models.CharField(validators=[MinLengthValidator(3)],max_length=10)
    is_capital =models.CharField(max_length=30)

    class Meta:
        db_table='State'

    def __str__(self):
        return f'{self.state_name}'


class City(Base):
    country=models.ForeignKey(Country,on_delete=models.CASCADE,related_name='city')
    state=models.ForeignKey(State,on_delete=models.CASCADE,related_name='city')
    city_name=models.CharField(max_length=20)
    short_name=models.CharField(validators=[MinLengthValidator(3)],max_length=10)

    class Meta:
        db_table='City'

    def __str__(self):
        return f'{self.country.country_name} {self.state.state_name} {self.city_name}'
    

    
    