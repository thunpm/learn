from django.views.generic import ListView, DetailView
from .models import Publisher

class PublisherListView(ListView):
    model = Publisher

class PublisherDetailView(DetailView):
    queryset = Publisher.objects.all()
