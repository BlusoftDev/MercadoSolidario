from django.contrib import admin
from .models import Banner

# Register your models here.

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):

    #Permite que solo exista un Banner
    def has_add_permission(self, request):
        retVal = super(BannerModelAdmin, self).has_add_permission(request)
        if retVal and Banner.objects.exists():
            retVal = False
        return retVal

    class Media:
        js = (
            'core/js/admin.js',
        )
