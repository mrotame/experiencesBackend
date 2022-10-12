from django.test import TestCase

from main.tests import DefaultTestCase
# Create your tests here.

class SetupTest(DefaultTestCase, TestCase):
    pass

class TestExperienciasView(SetupTest):
    def setUp():