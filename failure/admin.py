from django.contrib import admin
from datetime import datetime
from failure.models import Hala, Wydzial, Maszyna, Status, Awaria

class HalaAdmin(admin.ModelAdmin):
	list_display = ["symbol","user"]
	list_filter = ["user"]
	list_display_links = ["symbol"]
	ordering = ["id"]

class WydzialAdmin(admin.ModelAdmin):
	list_display = ["nazwa","user"]
	list_filter = ["user"]
	list_display_links = ["nazwa"]
	ordering = ["nazwa"]
	search_fields = ["nazwa"]

class MaszynaAdmin(admin.ModelAdmin):
	list_display = ["nazwa", "wydzial", "hala", "opiekun"]
	list_filter = ["wydzial", "hala", "opiekun"]
	list_display_links = ["nazwa"]
	search_fields = ["nazwa"]
	ordering = ["id"]

class StatusAdmin(admin.ModelAdmin):
	list_display = ["nazwa"]
	list_display_links = ["nazwa"]
	ordering = ["id"]

class AwariaAdmin(admin.ModelAdmin):
	list_display = ["maszyna", "wydzial", "description", "add_date", "user", "sur", "repair_date", "remove_date", "status"]
	exclude = ["user","add_date"]
	list_filter = ["wydzial", "add_date", "status"]
	list_display_links = ["status"]
	search_fields = ["maszyna", "sur"]
	ordering = ("status", "-add_date")

	def save_model(self, request, obj, form, change):
         obj.user = request.user
         obj.save()

admin.site.register(Hala, HalaAdmin)
admin.site.register(Wydzial, WydzialAdmin)
admin.site.register(Maszyna, MaszynaAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Awaria, AwariaAdmin)
