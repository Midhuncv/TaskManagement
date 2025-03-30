from django.urls  import path,include
from rest_framework.routers import DefaultRouter
from .views import*


router = DefaultRouter()
router.register(r'RegisterViewSet',RegisterViewSet,basename='RegisterViewSet'),
router.register(r'Login',Login,basename='Login'),
router.register(r'TaskView',TaskView,basename='TaskView')
router.register(r'ResetPasswordView',ResetPasswordView,basename='ResetPasswordView')


urlpatterns = [
   
    path('',include(router.urls)),
    
]