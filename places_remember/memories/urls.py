from django.urls import path
from .views import (
    MemoryListView,
    MemoryCreateView,
    MemoryDetailView,
    MemoryDeleteView,
    MemoryUpdateView,
)


urlpatterns = [
    # path('', show_main_page()),
    path("", MemoryListView.as_view(), name="memories"),
    path("create", MemoryCreateView.as_view(), name="create"),
    path("<int:pk>", MemoryDetailView.as_view(), name="detail"),
    path("<int:pk>/delete", MemoryDeleteView.as_view(), name="delete"),
    path("<int:pk>/edit", MemoryUpdateView.as_view(), name="edit"),
]
