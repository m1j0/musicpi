from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static
from title import views

urlpatterns = patterns(
    '',
    url(r'^$', views.TitleListView.as_view()),
    url(r'add/$', views.CreateView.as_view())
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
