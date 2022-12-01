from django import forms

from room_booking.models import WishList


class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        exclude = ['']



class WishList(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    check_in = models.DateTimeField(blank=True, null=True)
    check_out = models.DateTimeField(blank=True, null=True)
    room_cleaning = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    breakfast = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)

    def __str__(self):
        return f"{self.room.room_number} {self.room.style}"