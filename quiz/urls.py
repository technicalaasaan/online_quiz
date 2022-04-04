from rest_framework.routers import DefaultRouter
from .views import QuizViewSet

quiz_router = DefaultRouter()
quiz_router.register('add_question', QuizViewSet)