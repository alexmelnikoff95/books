from django.contrib import admin

from books.models import Band, Artist

admin.site.register(Artist)
admin.site.register(Band)
