import json
from rest_framework import status
from rest_framework.reverse import reverse
from django.contrib.staticfiles.finders import find
from rest_framework.test import APITestCase


class TestCategories(APITestCase):

    def setUp(self):
        example_request_file_path = find('categoriestree/tests/example_request.json')
        example_response_file_path_id2 = find('categoriestree/tests/example_response_id2.json')
        example_response_file_path_id8 = find('categoriestree/tests/example_response_id8.json')
        with open(example_request_file_path, 'r') as request_file_fp, open(example_response_file_path_id2, 'r') \
                as response_file_id2_fp, open(example_response_file_path_id8, 'r') \
                as response_file_id8_fp:
            self.example_post_request_data = json.load(request_file_fp)
            self.example_response_data_id2 = json.load(response_file_id2_fp)
            self.example_response_data_id8 = json.load(response_file_id8_fp)

    def __init_data(self):
        url = reverse('categoriestree:category-list')
        self.client.post(url, self.example_post_request_data, format='json')

    def __ordered_dict_data(self):
        url = reverse('categoriestree:category-list')
        self.client.post(url, self.example_post_request_data, format='json')

    def test_post(self):
        """
        test create new categories tree
        """
        url = reverse('categoriestree:category-list')
        response = self.client.post(url, self.example_post_request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get(self):
        """
        test get categories tree
        """
        self.__init_data()
        url = reverse('categoriestree:category-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail(self):
        """
        test get detail categories branch
        """
        self.__init_data()
        url = reverse('categoriestree:category-detail', args=(2,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.example_response_data_id2)

        url = reverse('categoriestree:category-detail', args=(8,))
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.example_response_data_id8)
