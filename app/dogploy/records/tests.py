from django.test import TestCase
from records.models import Vet, Animal, Owner

class VetTestCase(TestCase):
    def setUp(self):
        Vet.objects.create(first_name="Docker", last_name="Whalius")
        Vet.objects.create(first_name="B0G7S", last_name="N0T4DOC")
        
    def test_vet_introduction(self):
        """Vets can properly introduce themselves"""
        dock = Vet.objects.get(first_name = "Docker")
        B0G = Vet.objects.get(first_name = "B0G7S")
        self.assertEqual(dock.introduce(), "Hello, I am Docker Whalius")
        self.assertEqual(B0G.introduce(), "Hello, I am B0G7S N0T4DOC")

class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(species="axolotl", age=1, owner="Kenobi")
        Animal.objects.create(species="kangaroo", age=5, owner="Mars")

    def test_animal_introduction(self):
        axo = Animal.objects.get(species = "axolotl")
        kang = Animal.objects.get(species = "kangaroo")
        self.assertEqual(axo.introduce(), "I am a 1-year old axolotl owned by Kenobi")
        self.assertEqual(kang.introduce(), "I am a 5-year old kangaroo owned by Mars")

class OwnerTestCase(TestCase):
    def setUp(self):
        Owner.objects.create(name="Crozet Pizza", address="1111 Somewhere Elliewood")
        Owner.objects.create(name="Tony Bennett (the singer)", address="321 Outside World")

    def test_owner_introduction(self):
        crozet = Owner.objects.get(name="Crozet Pizza")
        tony = Owner.objects.get(name = "Tony Bennett (the singer)")
        self.assertEqual(crozet.introduce(), "I am Crozet Pizza and I live at: 1111 Somewhere Elliewood")
        self.assertEqual(tony.introduce(), "I am Tony Bennett (the singer) and I live at: 321 Outside World")

#class AnimalTestCase(TestCase):
#    def setUp(self):
#        Animal.objects.create(name="lion", sound="roar")
#        Animal.objects.create(name="cat", sound="meow")
#
#    def test_animals_can_speak(self):
#        """Animals that can speak are correctly identified"""
#        lion = Animal.objects.get(name="lion")
#        cat = Animal.objects.get(name="cat")
#        self.assertEqual(lion.speak(), 'The lion says "roar"')
#        self.assertEqual(cat.speak(), 'The cat says "meow"')
