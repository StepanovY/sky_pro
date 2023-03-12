import pytest
from django.urls import reverse


@pytest.mark.django_db
def test_resume_update(
        user,
        get_auth_client,
        resume_factory,
):
    resume = resume_factory(author=user)
    data = {
        'title': 'title',
    }

    auth_client = get_auth_client(user=user)
    url = reverse('resume_update', kwargs={'pk': resume.pk})
    response = auth_client.patch(path=url, data=data)

    expected_response = {
        'id': 1,
        'status': 1,
        'grade': '1',
        'specialty': 'python',
        'salary': None,
        'education': 'education',
        'experience': 'experience',
        'portfolio': None,
        'title': 'title',
        'phone': '',
        'email': 'email',
        'author': 1

    }

    assert response.status_code == 200
    assert response.data == expected_response
