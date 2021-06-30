from django.contrib import admin
from .models import news,newsdate,RegistrationData,InfoData,Response

# Register your models here.
admin.site.register(news)
admin.site.register(newsdate)
admin.site.register(RegistrationData)
admin.site.register(InfoData)
admin.site.register(Response)