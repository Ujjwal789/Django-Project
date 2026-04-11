from django.contrib import admin
from .models import chaivarity, Review, Order, store,Profile

# Register your models here.
class chaiReviewInline(admin.TabularInline):
    model = Review
    extra = 1

class chaivarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date_added')
    search_fields = ('name', 'type')
    list_filter = ('type', 'date_added','reviews__rating')
    inlines = [chaiReviewInline]

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_ordered')
    search_fields = ('user__username',)
    list_filter = ('date_ordered',)
    filter_horizontal = ('chaivarity',)

class storeAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'date_opened')
    filter_horizontal = ('chaivarity',)
    

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'date_added')
    search_fields = ('user__username', 'bio', 'date_added')
    list_filter = ('date_added',)


admin.site.register(chaivarity, chaivarityAdmin)
admin.site.register(Review)
admin.site.register(Order, OrderAdmin)
admin.site.register(store, storeAdmin)
admin.site.register(Profile, ProfileAdmin)
