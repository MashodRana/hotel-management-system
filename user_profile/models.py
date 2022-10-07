from django.db import models


class Person(models.Model):
    ACCOUNT_TYPES = (
        ('admin','Admin'),
        ( 'manager', 'Manager'),
        ( 'receptionist' ,'Receptionist'),
        ( 'guest' ,'Guest'),
        ( 'stuff','Stuff')
    )
    
    name = models.CharField(max_length=64)
    email = models.EmailField()
    phone = models.CharField(max_length=16)
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES)

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    zip_code = models.IntegerField()
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.person.name}, {self.city}, {self.country}"


class Account(models.Model):
    password = models.CharField(max_length=16)
    status = models.BooleanField(default=True)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.person.name

