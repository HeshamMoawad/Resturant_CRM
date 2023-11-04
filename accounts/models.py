from django.db import models


# Create your models here.
class City(models.Model):
    # creator = 
    name = models.CharField(max_length=50)
    created_at = models.DateField(verbose_name="Created At",auto_now=True)

    def __str__(self) -> str:
        return f"{self.name}"
    
    class Meta:
        verbose_name = 'City'
        verbose_name_plural = "Cities"


class Area(models.Model):
    # creator = 
    name = models.CharField(max_length=50)
    city = models.ForeignKey(City,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.city} : {self.name}"
    
    class Meta:
        verbose_name = 'Area'
        verbose_name_plural = "Areas"



class Account(models.Model):
    # creator = 
    name = models.CharField(max_length=50 )
    phone_number =  models.CharField(max_length=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} : {self.phone_number}"
    
    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = "Accounts"




class Address(models.Model): 
    # creator = 
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name="addresses")                                                  
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)
    street = models.CharField(max_length=50 , blank=True)
    building = models.CharField(max_length=50)
    floor = models.CharField(max_length=50 , blank=True)
    apartment = models.CharField(max_length=50 , blank=True)
    landmark = models.CharField(max_length=50 , blank=True)

    def __str__(self) -> str:
        return f"{self.account} - {self.area} : {self.building}"
    
    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = "Addresses"
