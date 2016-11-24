from django.contrib import admin
from models import *
from actions import export_as_csv



class EnlaceAdmin(admin.ModelAdmin):
	list_display = ('titulo', 'enlace','categoria', 'imagen_voto', 'es_popular',)
	list_filter = ('categoria', 'usuario')
	search_fields = ('categoria__titulo', 'usuario__email')
	list_editable = ('titulo', 'enlace', 'categoria')
	list_display_links = ('es_popular',)
	actions = [export_as_csv]
	raw_id_fields = ('categoria', 'usuario', )

	def imagen_voto(self, obj):
		url = obj.ima_ros()
		tag = '<img src="%s" />' % (url)
		return tag
	imagen_voto.allow_tags = True
	imagen_voto.admin_order_field = 'votos'	

class EnlaceInline(admin.StackedInline):
	model = Enlace
	extra = 2
	raw_id_fields = ('usuario',)
class CategoriaAdmin(admin.ModelAdmin):
	actions = [export_as_csv]
	inlines = [EnlaceInline]

class CompradorAdmin(admin.ModelAdmin):
	filter_horizontal = ('enlace', )		

admin.site.register(Comprador, CompradorAdmin)
admin.site.register(Categoria,CategoriaAdmin)

