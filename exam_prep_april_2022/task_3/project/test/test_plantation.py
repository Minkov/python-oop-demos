import unittest

from project.plantation import Plantation


class PlantationTests(unittest.TestCase):
    valid_size = 1000
    invalid_size = -1

    def setUp(self) -> None:
        self.plantation = Plantation(self.valid_size)

    def test_init__when_size_is_1__expect_correct_values(self):
        self.assertEqual(self.valid_size, self.plantation.size)
        self.assertDictEqual({}, self.plantation.plants)
        self.assertListEqual([], self.plantation.workers)

    def test_size_prop__when_value_is_0__expect_correct(self):
        plantation = Plantation(self.valid_size)
        plantation.size = self.valid_size + 1

        self.assertEqual(plantation.size, self.valid_size + 1)

    def test_size_prop__when_value_is_negative__expect_to_raise(self):
        with self.assertRaises(ValueError) as context:
            self.plantation.size = self.invalid_size

        self.assertIsNotNone(context.exception)
        self.assertEqual('Size must be positive number!', str(context.exception))
        self.assertEqual(self.valid_size, self.plantation.size)

    def test_hire_worker__when_new_worker__expect_success(self):
        worker = 'Worker'
        result = self.plantation.hire_worker(worker)
        self.assertEqual(f"{worker} successfully hired.", result)
        self.assertIn(worker, self.plantation.workers)

    def test_hire_worker__when_existing_worker__expect_to_raise(self):
        worker = 'Worker'
        self.plantation.hire_worker(worker)
        with self.assertRaises(ValueError) as context:
            self.plantation.hire_worker(worker)
        self.assertIsNotNone(context.exception)
        self.assertEqual('Worker already hired!', str(context.exception))

    def test_len_no_plants(self):
        pass

    def test_len_with_plants(self):
        pass

    def test_str__when_no_workers__expect_correct(self):
        expected = f"""Plantation size: {self.valid_size}
"""
        actual = str(self.plantation)

        self.assertEqual(expected, actual)

    def test_str__when_workers_and_no_plants__expect_correct(self):
        workers = ['Worker 1', 'Worker 2']
        [self.plantation.hire_worker(w) for w in workers]
        expected = f"""Plantation size: {self.valid_size}
Worker 1, Worker 2"""
        actual = str(self.plantation)

        self.assertEqual(expected, actual)

    def test_str__when_workers_and_plants__expect_correct(self):
        workers = ['Worker 1', 'Worker 2']
        plants = ['plant 1', 'plant 2']
        plant3 = 'plant3'
        [self.plantation.hire_worker(w) for w in workers]
        [self.plantation.planting(workers[0], p) for p in plants]
        self.plantation.planting(workers[1], plant3)
        expected = f"""Plantation size: {self.valid_size}
Worker 1, Worker 2
Worker 1 planted: {", ".join(plants)}
Worker 2 planted: {plant3}"""
        actual = str(self.plantation)

        self.assertEqual(expected, actual)

    def test_repr_no_workers(self):
        pass

    def test_repr_workers(self):
        pass

    def test_planting__when_worker_not_exist__expect_to_raise(self):
        worker = 'Worker'
        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, '')

        self.assertEqual(
            f'Worker with name {worker} is not hired!',
            str(context.exception))

    def test_planting__when_full__expect_to_raise(self):
        worker = 'Worker'
        self.plantation.size = 0
        self.plantation.hire_worker(worker)

        with self.assertRaises(ValueError) as context:
            self.plantation.planting(worker, 'plant')

        self.assertEqual(
            f'The plantation is full!',
            str(context.exception))

    def test_planting__when_worker_has_plants__expect_success(self):
        worker = 'Worker'
        plant1 = 'plant1'
        plant2 = 'plant2'
        self.plantation.hire_worker(worker)
        self.plantation.planting(worker, plant1)
        result = self.plantation.planting(worker, plant2)

        self.assertDictEqual(
            {worker: [plant1, plant2]},
            self.plantation.plants
        )
        self.assertEqual(
            f'{worker} planted {plant2}.',
            result
        )

    def test_planting__when_worker_has_no_plants__expect_success(self):
        worker = 'Worker'
        plant = 'plant'
        self.plantation.hire_worker(worker)
        result = self.plantation.planting(worker, plant)

        self.assertDictEqual(
            {worker: [plant]},
            self.plantation.plants
        )
        self.assertEqual(
            f'{worker} planted it\'s first {plant}.',
            result
        )
