from django.contrib import admin
from .models import Barang
# Register your models here.

class BarangAdmin(admin.ModelAdmin):
    list_display = ('kodebrg','nama','stok','harga')
    list_filter = ('kodebrg', 'nama')
    search_fields = ('nama', 'harga')

admin.site.register(Barang, BarangAdmin)