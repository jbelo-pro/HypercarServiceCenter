from django.shortcuts import render
from django.views import View


class ReviewView(View):
    reviews = ['dfd']  # List of reviews as plain strings

    def get(self, request, *args, **kwargs):
        context = {'reviews': self.reviews}
        return render(request, 'book/reviews.html', context=context)
