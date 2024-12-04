from django.urls import path
from .views import (
    ChooseCA, VerifyWebsite, GenerateCSR, SubmitCSR,
    InstallCertificate, RedirectToHTTPS, CheckSSL
)

urlpatterns = [
    path('choose_ca/', ChooseCA.as_view(), name='choose_ca'),
    path('verify_website/', VerifyWebsite.as_view(), name='verify_website'),
    path('generate_csr/', GenerateCSR.as_view(), name='generate_csr'),
    path('submit_csr/', SubmitCSR.as_view(), name='submit_csr'),
    path('install_certificate/', InstallCertificate.as_view(), name='install_certificate'),
    path('redirect_to_https/', RedirectToHTTPS.as_view(), name='redirect_to_https'),
    path('check_ssl/', CheckSSL.as_view(), name='check_ssl'),
]
