from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from genre.views import ListGenre, CreateGenre

urlpatterns = patterns(
    '',
    url(r'^$', ListGenre.as_view()),
    url(r'add/$', CreateGenre.as_view())
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
