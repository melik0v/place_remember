from django.urls import path
from .views import MemoryListView, MemoryCreateView, MemoryDetailView


urlpatterns = [
    # path('', show_main_page()),
    path("", MemoryListView.as_view(), name="memories"),
    path("create", MemoryCreateView.as_view(), name="create"),
    path("<int:pk>", MemoryDetailView.as_view(), name="detail"),
]
