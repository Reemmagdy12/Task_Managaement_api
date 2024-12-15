from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
   

urlpatterns = [

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

from django.urls import path
from .views import CreateTaskView

urlpatterns = [
    path('tasks/create/', CreateTaskView.as_view(), name='create-task'),
]

from .views import ListTasksView

urlpatterns += [
    path('users/<int:user_id>/tasks/', ListTasksView.as_view(), name='list-tasks'),
]