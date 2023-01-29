from django.shortcuts import render
from django.views import View

from books_site.books.helper import IsStaffPerm


class IndexView(IsStaffPerm, View):

    def get(self, request):
        return render(request, 'index.html')
