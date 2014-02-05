from django.views.generic import ListView, DetailView

from .models import Location

class LocationsByState(ListView):
    def get_queryset(self):
        self.state = self.kwargs.get('state', None)
        if self.state is None:
            return Location.objects.none
        else:
            return Location.objects.filter(state=self.state).order_by('city')

    def get_context_data(self, **kwargs):
        context = super(LocationsByState, self).get_context_data(**kwargs)
        context['state'] = self.state
        return context

class LocationDetail(DetailView):
    model = Location
