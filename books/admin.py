from django.contrib import admin

# Register your models here.
from books.models import Artist, Band

admin.site.register(Artist)
admin.site.register(Band)
