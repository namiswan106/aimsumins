from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Service, Blog, Testmonial, Faq ,Portfolio,PortfolioCategory,Contact,Client_logo,Team,Counter ,Main


class ImagePreviewAdminMixin:
    def image_preview(self, obj):
        if obj.image:
            return mark_safe(
                f'<img loading="lazy" src="{obj.image.url}" style="width:50px;height:50px;object-fit:contain;">'
            )
        return None

    image_preview.short_description = "Image Preview"
    
    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin,ImagePreviewAdminMixin):
    list_display = ("title", "image_preview")
    prepopulated_fields = {"slug": ("title",)}
    

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin,ImagePreviewAdminMixin):
    list_display = ("title", "image_preview")
    prepopulated_fields = {"slug": ("title",)}
    
    
@admin.register(Testmonial)
class TestmonialAdmin(admin.ModelAdmin):
    list_display = ("name", "position")
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question',)
    
    
    
class PortfolioInline(admin.TabularInline):
    model = Portfolio
    extra = 1
    fields = ('title','subtitle','image')
        
# @admin.register(PortfolioCategory)
# class PortfolioCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     inlines = [PortfolioInline]
    

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin,ImagePreviewAdminMixin):
    list_display = ("image_preview",)
    
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name','email','phone')
    
@admin.register(Client_logo)
class ClientLogoAdmin(admin.ModelAdmin,ImagePreviewAdminMixin):
    list_display = ("image_preview",)


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin,ImagePreviewAdminMixin):
    list_display = ('name','position','image_preview')
    
    
@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('title','number','plus_icon')
    
@admin.register(Main)
class MainAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Banner', {
            'fields': ('banner_title', 'banner_image', 'banner_description'),
        }),
        ('About', {
            'fields': ('about_title', 'about_image', 'about_description'),
        }),
    )