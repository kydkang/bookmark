from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns 


urlpatterns = i18n_patterns(                     ## for language switching -- django4ByExample p499 ##
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')), 

    path('', RedirectView.as_view(url='account/')), ## OR redirect to a main app

    path('rosetta/', include('rosetta.urls')), 
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
