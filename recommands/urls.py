from django.urls import include, path, re_path
from . import views


urlpatterns = [
    re_path(r'^api/v1/recommands/(?P<pk>[0-9]+)$',  # Url to get update or delete a recommand
        views.get_delete_update_recommand.as_view(),
        name='get_delete_update_recommand'
    ),
    path('api/v1/recommands/',  # urls list all and create new one
        views.get_post_recommands.as_view(),
        name='get_post_recommands'
    )
]