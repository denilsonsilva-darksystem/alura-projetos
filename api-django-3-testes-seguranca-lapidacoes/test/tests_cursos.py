from rest_framework.test import APITestCase
from escola.models import Curso
from django.urls import reverse


class CursosTestCases(APITestCase):

    def setUp(self):
        self.list_url = reverse('Cursos-list')
        self.curso_1 = Curso.objects.create(
            codigo_curso='CT1', descricao='Curso Teste 1', nivel='B'
        )
        self.curso_2 = Curso.objects.create(
            codigo_curso='CT2', descricao='Curso Teste 2', nivel='A'
        )

    def test_falhador(self):
        self.fail('Falhou de proposito')