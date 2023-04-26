
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from malayanfolio import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("__reload__/", include("django_browser_reload.urls")),

    path("account/", include("accounts.urls")),
    path("profiles/", include("profiles.urls")),
    path(
        "", views.Home, name="home"
    ),
    path(
        "profile/view_profile/<user_id>", views.ViewProfile, name="profile"
    ),
    path(
        "profile/search/accounts", views.ProfileSearch, name="profile-search"
    ),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#ERROR HANDLER
handler404 = 'malayanfolio.views.handler404'
handler500 = 'malayanfolio.views.handler500'
