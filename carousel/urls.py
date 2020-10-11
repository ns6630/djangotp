from django.urls import path

from carousel import views

urlpatterns = [
    path('', views.CarouselPageView.as_view(), name='carousel_page'),
]