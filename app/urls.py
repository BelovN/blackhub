from django.urls import re_path
from django.views.decorators.csrf import csrf_exempt

from .views import BlackhubView

urlpatterns = [
    # all uri path into one view
    re_path(r"^.*$", csrf_exempt(BlackhubView.as_view())),
]
