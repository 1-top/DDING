from django.contrib import admin

from store.models import Store, Category, Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'location', 'name', 'category')


admin.site.register(Report, ReportAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Category, CategoryAdmin)


class StoreAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude', 'location', 'name', 'category')


admin.site.register(Store, StoreAdmin)
