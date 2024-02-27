from django.contrib import admin
from .models import B_Client

class PostAdmin(admin.ModelAdmin):
    list_display = ('name_second_name', 'loyalty_card', 'id_user', 'created_date', 'telephone_num')

admin.site.register(B_Client, PostAdmin)