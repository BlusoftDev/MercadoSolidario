from django.contrib import admin
from .models import Payment,City,Locality,Colony,Activity, SubActivity, Company


# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

class CityAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

class LocalityAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

class ColonyAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

class ActivityAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

class SubActivityAdmin(admin.ModelAdmin):
        readonly_fields = ('created', 'updated')

        class Meta:
                model = Activity
                exclude = ('id', )
                import_id_fields = ('name',)
            

class CompanyAdmin(admin.ModelAdmin):
        readonly_fields = ('created',)
        list_display = ('name', 'city', 'colony', 'get_activity')
        ordering = ('name', 'city')
        search_fields = ('name','city', 'colony', 'get_activity')
        date_hierarchy = 'created'
        list_filter = ('city','subactivity__activity')
        change_list_template = 'admin/companies/companies_change_list.html'

        def get_activity(self, obj):
                return obj.subactivity.activity
        get_activity.short_description = 'Actividad'
        get_activity.admin_order_field = 'subactivity__activity'
        

        
admin.site.register(Payment, PaymentAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(Colony, ColonyAdmin)
admin.site.register(Activity, ActivityAdmin)
admin.site.register(SubActivity, SubActivityAdmin)
admin.site.register(Company, CompanyAdmin)
