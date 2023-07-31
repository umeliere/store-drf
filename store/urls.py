from django.urls import path

from store.views import ProductsListView, ReviewCreateView

app_name = 'store'
urlpatterns = [
    path('products/', ProductsListView.as_view()),
    path("reviews/", ReviewCreateView.as_view()),
]
