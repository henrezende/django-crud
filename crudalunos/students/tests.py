""" Students tests """
import json
from django.test import TestCase
from rest_framework import status
from crudalunos.students.serializers import StudentSerializer
from crudalunos.students.models import Student
from crudalunos.subjects.models import Subject


class ListAllStudentTestCase(TestCase):
    """ Test of the Student list methods, with and without filter """

    def setUp(self):
        Student.objects.create(
            first_name="John",
            last_name="Doe",
            registration_number="ABC1234",
        )
        Student.objects.create(
            first_name="Jane",
            last_name="Doe",
            registration_number="DEF5678",
        )

    def test_list_all_students(self):
        """List all students without a filter"""
        response = self.client.get('/students/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['count'], 2)

    def test_list_filtered_students(self):
        """List all students using a filter"""
        response = self.client.get(
            '/students/', {'registration_number': 'DEF5678'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content)['count'], 1)


class ShowSingleStudentTestCase(TestCase):
    """ Test of the Student show methods """

    def setUp(self):
        self.john = Student.objects.create(
            first_name="John",
            last_name="Doe",
            registration_number="ABC1234",
        )

    def test_show_valid_student(self):
        """Show a valid student"""
        response = self.client.get(f'/students/{self.john.pk}/', format='json')
        student_obj = Student.objects.get(id=self.john.pk)
        serializer = StudentSerializer(student_obj)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_show_invalid_student(self):
        """Trying to show a invalid student"""
        response = self.client.get('/students/50/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateStudentTestCase(TestCase):
    """ Test of the Student create methods """

    def setUp(self):
        self.math = Subject.objects.create(name="Math")
        self.english = Subject.objects.create(name="English")

    def test_create_valid_student_without_subjects(self):
        """Creates a valid student via API"""
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "registration_number": "123456",
        }
        response = self.client.post(
            '/students/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_valid_student_with_subjects(self):
        """Creates a valid student with subjects via API"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "registration_number": "654321",
            "subjects": [
                self.math.pk, self.english.pk
            ]
        }
        response = self.client.post(
            '/students/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_student(self):
        """Try to create a student with invalid payload"""
        data = {
            "first_name": "Jorge",
            "last_name": "",
            "registration_number": "564738"
        }
        response = self.client.post(
            '/students/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateStudentTestCase(TestCase):
    """ Test of the Student update methods """

    def setUp(self):
        self.john = Student.objects.create(
            first_name="John doe",
            last_name="Doe",
            registration_number="ABC1234",
        )
        self.math = Subject.objects.create(name="Math")

    def test_valid_patch_update_student(self):
        """Updates a student with valid data"""
        data = {
            "first_name": "John"
        }
        response = self.client.patch(
            f'/students/{self.john.pk}/', data, format='json', content_type='application/json')

        student_obj = Student.objects.get(id=self.john.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(student_obj.first_name, "John")

    def test_invalid_patch_update_student(self):
        """Updates a student with invalid data"""
        data = {
            "first_name": ""
        }
        response = self.client.patch(
            f'/students/{self.john.pk}/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_put_update_student_with_subject(self):
        """Updates a student with valid data"""
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "registration_number": "ABC1234",
            "subjects": [self.math.pk]
        }
        response = self.client.put(
            f'/students/{self.john.pk}/', data, format='json', content_type='application/json')

        student_obj = Student.objects.get(id=self.john.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(student_obj.first_name, "John")

    def test_valid_put_update_student_without_subject(self):
        """Updates a student with valid data"""
        data = {
            "first_name": "Johnny",
            "last_name": "Doe",
            "registration_number": "ABC1234",
        }
        response = self.client.put(
            f'/students/{self.john.pk}/', data, format='json', content_type='application/json')

        student_obj = Student.objects.get(id=self.john.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(student_obj.first_name, "Johnny")

    def test_invalid_put_update_student(self):
        """Updates a student with invalid data"""
        data = {
            "first_name": "",
            "last_name": "Doe",
            "registration_number": "ABC1234",
        }
        response = self.client.put(
            f'/students/{self.john.pk}/', data, format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteStudentTestCase(TestCase):
    """ Test of the Student delete methods """

    def setUp(self):
        self.john = Student.objects.create(
            first_name="John doe",
            last_name="Doe",
            registration_number="ABC1234",
        )

    def test_valid_delete_student(self):
        """Delete a student with valid data"""
        response = self.client.delete(
            f'/students/{self.john.pk}/', format='json', content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_student(self):
        """Delete a student with invalid data"""
        response = self.client.delete(
            '/students/50/', format='json', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
