from django.contrib import admin
from home.models import ContactFormMessage, Setting

from home.models import Setting, UserProfile

admin.site.register(Setting)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user_name','address','phone','city','country','image_tag']

admin.site.register(UserProfile, UserProfileAdmin)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name','subject','update_at','status'] #! görüntülenecek kısım.
    readonly_fields = ('name','subject','email','message','ip') #! düzenleme yapılamayacak olanlar.
    list_filter = ['status']
    #! fields = ['name','subject'] # sadece bu kısımlar görünür.
admin.site.register(ContactFormMessage, ContactFormMessageAdmin)