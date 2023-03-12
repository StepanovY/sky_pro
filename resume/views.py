from rest_framework.generics import ListAPIView, UpdateAPIView

from resume.models import Resume
from resume.permissions import ResumeUpdatePermission
from resume.serializers import ResumeListSerializer, ResumeUpdateSerializer


class ResumeView(ListAPIView):
    """
    Просмотр резюме.
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeListSerializer


class ResumeUpdateView(UpdateAPIView):
    """
    Редактирование своего резюме пользователем.
    """
    queryset = Resume.objects.all()
    permission_classes = [ResumeUpdatePermission]
    serializer_class = ResumeUpdateSerializer
