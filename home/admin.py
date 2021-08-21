from django.contrib import admin
from .models import *
# Register your models here.
class ChoiceAdmin(admin.StackedInline):
    model = Itinerary

class ImageAdmin (admin.StackedInline):
    model = Treck_Image

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceAdmin, ImageAdmin ]
    



admin.site.register(trekcategory)

admin.site.register(Treck,QuestionAdmin)
admin.site.register(Itinerary)
admin.site.register(review)
admin.site.register(Boodtreck)