
import unittest

from module_12.runner_and_tournament_classes import Runner, Tournament


class TournamentTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner('Husein', 10)
        self.runner2 = Runner('Nick', 3)
        self.runner3 = Runner('Andre', 9)

    @classmethod
    def tearDownClass(cls):
        for test_key, test_value in cls.all_results.items():
            tour_dict = {}
            for key, value in test_value.items():
                chap = {key: value}
                tour_dict.update(chap)
            print(tour_dict)



    def tests_1(self):
        tour1 = Tournament(90,self.runner1, self.runner2)
        self.distance = tour1.start()
        self.all_results['first the race'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Nick')

    def tests_2(self):
        tour1 = Tournament(90, self.runner3, self.runner2)
        self.distance = tour1.start()
        self.all_results['second the race'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Nick')

    def tests_3(self):
        tour1 = Tournament(90, self.runner3, self.runner2, self.runner1)
        self.distance = tour1.start()
        self.all_results['third the race'] = self.distance
        self.assertEqual(self.distance[len(self.distance)], 'Nick')

