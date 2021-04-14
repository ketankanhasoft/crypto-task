from django.conf.urls import url
from cryptoAPI.views import (
    news_view
)

urlpatterns = [
    # settings
    url(r"^news/$", news_view.NewsList.as_view()),
]
