import pytest
from django.urls import reverse

from resume.serializers import ResumeListSerializer


@pytest.mark.django_db
def test_resume_list(
        user,
        get_auth_client,
        resume_factory,
):

    resume = resume_factory.create_batch(2)
    auth_client = get_auth_client(user)
    url = reverse('resume')
    response = auth_client.get(path=url)

    assert response.status_code == 200
    assert response.data == ResumeListSerializer(resume, many=True).data
