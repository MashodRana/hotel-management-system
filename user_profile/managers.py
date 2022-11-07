from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **other_fields):
        if not email:
            raise ValueError(_("The Email must be set"))
        
        email = self.normalize_email(email)
        user = self.model(email=email, **other_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **other_fields):
        ('admin','Admin'),
        ( 'manager', 'Manager'),
        ( 'receptionist' ,'Receptionist'),
        ( 'guest' ,'Guest'),
        ( 'stuff','Stuff')
        other_fields.setdefault("is_admin", True)
        other_fields.setdefault("is_manager", True)
        other_fields.setdefault("is_receptionist", True)
        other_fields.setdefault("is_guest", True)
        other_fields.setdefault("is_stuff", True)
        other_fields.setdefault("is_active", True)

        if other_fields.get('is_admin') is not True:
            raise ValueError(_('Admin must have is_admin=True.'))
        if other_fields.get('is_manager') is not True:
            raise ValueError(_('Admin must have is_manager=True.'))
        if other_fields.get('is_receptionist') is not True:
            raise ValueError(_('Admin must have is_receptionist=True.'))
        if other_fields.get('is_guest') is not True:
            raise ValueError(_('Admin must have is_guest=True.'))
        if other_fields.get('is_stuff') is not True:
            raise ValueError(_('Admin must have is_stuff=True.'))

        user = self.create_user(email, password, **other_fields)

        return user



