from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static
from btk_multishop import settings
import home


urlpatterns = [
    path('', include('home.urls')),    
    path('admin/', admin.site.urls),

    #? blog pages
    path('home/', include('home.urls')),
    path('product/', include('product.urls')),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('shop/', include('home.urls')),
    path('detail/', include('home.urls')),

    #? for the ckeditor
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

# To display images or static files on the admin side
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)