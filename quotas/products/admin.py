from django.contrib import admin

# Register your models here.
from .models import Product, Material, Weight
# from .forms import ProductCreate_Form


class Product_admin(admin.ModelAdmin):
    '''
        Admin View for Product Model
    '''
    # form = ProductCreate_Form
    # list_display = ('',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


class Material_admin(admin.ModelAdmin):
    '''
        Admin View for Material model
    '''
    # list_display = ('',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


class Weight_admin(admin.ModelAdmin):
    '''
        Admin View for Peso model  '''
    # list_display = ('',)
    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)


admin.site.register(Weight, Weight_admin)
admin.site.register(Material, Material_admin)
admin.site.register(Product, Product_admin)
