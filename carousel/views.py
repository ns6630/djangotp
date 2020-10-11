from django.shortcuts import render
from django.views.generic import TemplateView
from carousel.models import CarouselSlide


class CarouselPageView(TemplateView):

    template_name = 'carousel_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slides'] = CarouselSlide.objects.filter(is_active=True).order_by('order')
        return context
