from django.contrib import admin


from .models import Category,Comments,BlogList

admin.site.register([Category,Comments,BlogList])
