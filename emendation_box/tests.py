from django.test import TestCase
# Create your tests here.

from rest_framework.test import APIRequestFactory
from .models import EmendationBoxType
from .models import EmendationBoxStructure
from .views import EmendationBoxTypeListViewSet
from .views import EmendationBoxStructureListViewSet

class EmendationBoxTest(TestCase):

    def test_emendationbox_type(self):
        request = APIRequestFactory().get("")
        view = EmendationBoxTypeListViewSet.as_view(actions={'get': 'retrieve'})
        emendationbox_type = EmendationBoxType.objects.create(
            description="RandomEmendationBox")

        response = view(request, pk=emendationbox_type.pk)
        self.assertEqual(response.status_code, 200)

    def test_emendationbox_structure(self):
        request = APIRequestFactory().get("")
        view = EmendationBoxStructureListViewSet.as_view(actions={'get': 'retrieve'})
        emendationbox_structure = EmendationBoxStructure.objects.create(
            description="RandomEmendationBox")

        response = view(request, pk=emendationbox_structure.pk)
        self.assertEqual(response.status_code, 200)

    # def test_emendationbox(self):
    #    request = APIRequestFactory().get("")
    #    view = EmendationBoxListViewSet.as_view(actions={'get': 'retrieve'})
    #    emendationbox_type2 = EmendationBoxType.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox_structure2 = EmendationBoxStructure.objects.create(
    #        description="RandomEmendationBox2")
    #    emendationbox = EmendationBox.objects.create(
    #        lattitude=42,
    #        longitude=42,
    #        designNumber=13,
    #        access_box=True,
    #        creation_date=20170101,
    #        extinction_date=20180101,
    #        emendation_type = emendationbox_type2,
    #        emendation_structure = emendationbox_structure2)

    #    response = view(request, pk=emendationbox.pk)
    #    self.assertEqual(response.status_code, 200)

    # def test_emendationbox_delete(self):
    #    request = APIRequestFactory().get("")
    #    view = EmendationBoxListViewSet.as_view(actions={'get': 'retrieve'})
    #    emendationbox_type2 = EmendationBoxType.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox_structure2 = EmendationBoxStructure.objects.create(
    #        description="RandomEmendationBox")
    #    emendationbox = EmendationBox.objects.create(
    #        lattitude=42,
    #        longitude=42,
    #        designNumber=13,
    #        access_box=True,
    #        creation_date=20170101,
    #        extinction_date=20180101,
    #        emendation_type = emendationbox_type2,
    #        emendation_structure=emendationbox_type2)

    #    emendationbox.delete()
    #    response = view(request, pk=emendationbox.pk)
    #    self.assertEqual(response.status_code, 404)
