""" Subject tests """
import json
from rest_framework import status
from django.test import TestCase
from crudalunos.subjects.serializers import SubjectSerializer
from crudalunos.subjects.models import Subject


class ListAllSubjectTestCase(TestCase):
    """ Test of the Subject list methods """

    def setUp(self):
        Subject.objects.create(name="Math")
        Subject.objects.create(name="English")

    def test_list_all_subjects(self):
        """List all subjects"""
        response = self.client.get('/subjects/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['count'], 2)


class ShowSingleSubjectTestCase(TestCase):
    """ Test of the Subject show methods """

    def setUp(self):
        self.math = Subject.objects.create(name="Math")

    def test_show_valid_subject(self):
        """Show a valid subject"""
        response = self.client.get(f'/subjects/{self.math.pk}/', format='json')
        subject_obj = Subject.objects.get(id=self.math.pk)
        serializer = SubjectSerializer(subject_obj)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_show_invalid_subject(self):
        """Trying to show a invalid subject"""
        response = self.client.get('/subjects/50/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateSubjectTestCase(TestCase):
    """ Test of the Subject create methods """

    def setUp(self):
        self.math = Subject.objects.create(name="Math")
        self.english = Subject.objects.create(name="English")

    def test_create_valid_subject_without_subjects(self):
        """Creates a valid subject via API"""
        data = {
            "name": "Math",
        }
        response = self.client.post(
            '/subjects/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_subject(self):
        """Try to create a subject with invalid payload"""
        data = {
            "name": ""
        }
        response = self.client.post(
            '/subjects/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateSubjectTestCase(TestCase):
    """ Test of the Subject update methods """

    def setUp(self):
        self.math = Subject.objects.create(name="Math")

    def test_valid_patch_update_subject(self):
        """Updates a subject with valid data"""
        data = {
            "name": "Mathematics"
        }
        response = self.client.patch(
            f'/subjects/{self.math.pk}/', data, format='json', content_type='application/json')

        subject_obj = Subject.objects.get(id=self.math.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(subject_obj.name, "Mathematics")

    def test_invalid_patch_update_subject(self):
        """Updates a subject with invalid data"""
        data = {
            "name": ""
        }
        response = self.client.patch(
            f'/subjects/{self.math.pk}/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_put_update_subject(self):
        """Updates a subject with valid data"""
        data = {
            "name": "Mathematics"
        }
        response = self.client.put(
            f'/subjects/{self.math.pk}/', data, format='json', content_type='application/json')

        subject_obj = Subject.objects.get(id=self.math.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(subject_obj.name, "Mathematics")

    def test_invalid_put_update_subject(self):
        """Updates a subject with invalid data"""
        data = {
            "name": ""
        }
        response = self.client.put(
            f'/subjects/{self.math.pk}/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSubjectTestCase(TestCase):
    """ Test of the Subject delete methods """

    def setUp(self):
        self.math = Subject.objects.create(name="Math")

    def test_valid_delete_subject(self):
        """Delete a subject with valid data"""
        response = self.client.delete(
            f'/subjects/{self.math.pk}/', format='json', content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_subject(self):
        """Delete a subject with invalid data"""
        response = self.client.delete(
            '/subjects/50/', format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
