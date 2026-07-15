from rest_framework import viewsets, generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer, RegisterSerializer, EmptySerializer
from .permissions import IsAdminOrOwner
from rest_framework.filters import SearchFilter


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAdminOrOwner]
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['is_completed']
    search_fields = ['title', 'description']

    def get_queryset(self):
        user = self.request.user

        if hasattr(user, 'userprofile') and user.userprofile.role == 'admin':
            return Task.objects.all().order_by('-id')

        return Task.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # 🔥 BONUS: toggle API
    @action(detail=True, methods=['post'], serializer_class=EmptySerializer)
    def toggle(self, request, pk=None):
        task = self.get_object()
        task.is_completed = not task.is_completed
        task.save()

        return Response({
            'id': task.id,
            'is_completed': task.is_completed
        }, status=status.HTTP_200_OK)