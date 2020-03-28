from django.views.generic import TemplateView
from destinations.models import Destination, DestinationImage
from cities_light.models import City


class HomeView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        city = City.objects.get(name='Karachi')
        destination = Destination.objects.filter(city=city).order_by(
            '-created').first()
        default_image = DestinationImage.objects.filter(
            destination=destination).first()
        print(default_image.image)
        context['city_data'] = destination
        return context
