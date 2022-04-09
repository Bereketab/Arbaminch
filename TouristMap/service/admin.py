from django.contrib import admin
from .models import Service,ServiceImage
# Register your models here.
from django import forms
from .models import ServiceImage
# admin.site.register(Service)
# admin.site.register(ServiceImage)
class ServiceImageForm(forms.ModelForm):

    class Meta:
        model = ServiceImage
        fields = ('__all__')
        # labels = {
        #     'synset':'ሲንሴት',
        #     'definition':'ፍቺ',
        #     'pos':'የንግግር አካል',
        #     'example':'ምሳሌ',
        #     'meronymy':'ሜሪኖሚ'
        # }
        # widgets = {
        #     'colection': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        #     'definition': forms.Textarea(attrs={'cols': 20, 'rows': 3,}),
        #     'example': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        #     'meronymy': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        # }
class ServiceImageFormInline(admin.TabularInline):
    model = ServiceImage
    extra = 0
    form = ServiceImageForm
class ServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = ('__all__')
        # widgets = {
        #     'is_ambiguous': forms.CheckboxInput(attrs={'class': 'required checkbox form-control'}),
        # }
        # labels = {
        #     'word':'ቃል',
        #     'is_ambiguous':'አሻሚነው',
        # }
class SynsetWord(admin.ModelAdmin):
    inlines = [ServiceImageFormInline]
    form = ServiceForm
    list_per_page = 10
    # list_display = ('synset', 'definition', 'pos','example','meronymy')
    
 
    
admin.site.register(Service,SynsetWord)