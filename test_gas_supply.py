import unittest
from gas_supply import check_gas_supply

class TestPenguinGasSupply(unittest.TestCase):

    def test_all_cities_supplied(self):
        cities = ['Місто_1', 'Місто_2']
        storages = ['Сховище_А']
        pipes = [
            ['Сховище_А', 'Місто_1'],
            ['Місто_1', 'Місто_2']
        ]
        self.assertEqual(check_gas_supply(cities, storages, pipes), [])

    def test_partial_supply_failure(self):
        cities = ['Айсберг-Сіті', 'Снігове', 'Рибне']
        storages = ['Сховище_Північ', 'Сховище_Південь']
        pipes = [
            ['Сховище_Північ', 'Айсберг-Сіті'],
            ['Айсберг-Сіті', 'Снігове'],
            ['Сховище_Південь', 'Рибне']
        ]
        
        expected_result = [
            ['Сховище_Північ', ['Рибне']], 
            ['Сховище_Південь', ['Айсберг-Сіті', 'Снігове']]
        ]
        
        result = check_gas_supply(cities, storages, pipes)
        self.assertEqual(result, expected_result)

    def test_no_pipes_at_all(self):
        cities = ['Львів', 'Стрий']
        storages = ['Сховище_1']
        pipes = []
        
        expected_result = [
            ['Сховище_1', ['Львів', 'Стрий']]
        ]
        self.assertEqual(check_gas_supply(cities, storages, pipes), expected_result)

    def test_transit_through_other_cities(self):
        cities = ['М1', 'М2', 'М3', 'М4']
        storages = ['Сховище_Головне']
        pipes = [
            ['Сховище_Головне', 'М1'],
            ['М1', 'М2'],
            ['М2', 'М3'],
            ['М3', 'М4']
        ]
        self.assertEqual(check_gas_supply(cities, storages, pipes), [])

if __name__ == '__main__':
    unittest.main()