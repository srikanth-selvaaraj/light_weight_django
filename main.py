import sys
from django.conf import settings
from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import re_path as url

def index(request):
    return HttpResponse('Hello world!')

urlpatterns = [
    url(r'^$', index)
]


settings.configure(
    DEBUG=True,
    SECRET_KEY="mysecretkey",
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=[
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ],
)

if __name__ == "__main__":
    execute_from_command_line(sys.argv)
