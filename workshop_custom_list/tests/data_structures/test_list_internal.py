import unittest

from app.data_structures.list_internal import ListInternal


class ListInternalTests(unittest.TestCase):
    def test_append__when_list_is_empty__expect_to_has_single_value_and_returns_the_list(self):
        ll = ListInternal()
        value = 1
        result = ll.append(value)

        self.assertListEqual(
            [value],
            list(ll)
        )

        self.assertEqual(
            ll,
            result
        )

    def test_append__when_values_in_list__expect_to_has_one_more_value(self):
        ll = ListInternal()
        values = [1, 2, 3]
        result = [ll.append(v) for v in values]

        self.assertListEqual(
            values,
            list(ll)
        )

        self.assertListEqual(
            [ll] * len(values),
            result
        )

    def test_remove__when_single_value__expect_to_removed_the_value_and_empty_list(self):
        ll = ListInternal()
        value = 1
        index = 0
        ll.append(value)

        result = ll.remove(index)

        # Asserts the removed value is returned
        self.assertEqual(
            value,
            result
        )

        # Asserts the value is removed from the list
        self.assertListEqual(
            [],
            list(ll)
        )

    def test_remove__when_value_in_list__expect_to_be_removed(self):
        ll = ListInternal()
        value = 1
        values_to_add = [7, 2, 3, value, 6]
        index = values_to_add.index(value)
        [ll.append(v) for v in values_to_add]

        result = ll.remove(index)

        # Asserts the removed value is returned
        self.assertEqual(
            value,
            result
        )

        # Asserts the value is removed from the list
        self.assertListEqual(
            [7, 2, 3, 6],
            list(ll)
        )

    def test_remove__when_index_is_invalid__expect_to_raise_index_error(self):
        ll = ListInternal()
        values_to_add = [7, 2, 3, 6]
        [ll.append(v) for v in values_to_add]
        index = ll.size()  # invalid index

        with self.assertRaises(IndexError) as context:
            ll.remove(index)

        self.assertIsNotNone(context.exception)

    def test_remove__when_index_is_not_an_int__expect_to_raise_type_error(self):
        ll = ListInternal()
        index = '1'

        with self.assertRaises(TypeError) as context:
            ll.remove(index)

        self.assertIsNotNone(context.exception)
        self.assertEqual(
            'Index should be an integer',
            str(context.exception)
        )

    def test_get_by_index__when_index_is_valid__expect_to_return_correct_value(self):
        ll = ListInternal()
        value = 7
        values = [1, 2, 3, 4, value, 100]
        [ll.append(v) for v in values]
        index = values.index(value)

        result = ll[index]

        self.assertEqual(
            result,
            value
        )

    def test_get__when_index_is_valid__expect_to_return_correct_value(self):
        ll = ListInternal()
        value = 7
        values = [1, 2, 3, 4, value, 100]
        [ll.append(v) for v in values]
        index = values.index(value)

        result = ll.get(index)

        self.assertEqual(
            result,
            value
        )

    def test_get__when_index_is_negative_and_valid__expect_to_return_correct_value(self):
        ll = ListInternal()
        value = 7
        values = [1, 2, 3, 4, value, 100]
        [ll.append(v) for v in values]
        index = -2

        result = ll.get(index)

        self.assertEqual(
            result,
            value
        )

    def test_get__when_index_is_invalid__expect_to_raise_index_error(self):
        ll = ListInternal()
        values = [1, 2, 3, 4, 100]
        [ll.append(v) for v in values]
        index = ll.size()  # invalid index

        with self.assertRaises(IndexError) as context:
            ll.get(index)

        self.assertIsNotNone(context.exception)

    def test_get__when_index_is_negative_and_invalid__expect_to_raise_index_error(self):
        ll = ListInternal()
        values = [1, 2, 3, 4, 100]
        [ll.append(v) for v in values]
        index = -ll.size() - 1  # invalid index

        with self.assertRaises(IndexError) as context:
            ll.get(index)

        self.assertIsNotNone(context.exception)

    def test_get__when_list_is_empty__expect_to_raise_index_error(self):
        ll = ListInternal()
        index = 1

        with self.assertRaises(IndexError) as context:
            ll.get(index)

        self.assertIsNotNone(context.exception)

    def test_get__when_index_is_not_an_int__expect_to_raise_value_error(self):
        ll = ListInternal()
        index = '1'

        with self.assertRaises(TypeError) as context:
            ll.get(index)

        self.assertIsNotNone(context.exception)
        self.assertEqual(
            'Index should be an integer',
            str(context.exception)
        )

    def test_extend__when_both_lists_have_values__expect_extended_list(self):
        ll1 = ListInternal()
        ll2 = ListInternal()
        values1 = [1, 2, 3]
        values2 = [4, 5, 6]
        [ll1.append(v) for v in values1]
        [ll2.append(v) for v in values2]

        result = ll1.extend(ll2)

        self.assertEqual(
            ll1,
            result
        )

        self.assertListEqual(
            values1 + values2,
            list(ll1)
        )

    def test_extend__when__first_list_is_empty__expect_extended_list(self):
        ll1 = ListInternal()
        ll2 = ListInternal()
        values1 = []
        values2 = [4, 5, 6]
        [ll1.append(v) for v in values1]
        [ll2.append(v) for v in values2]

        result = ll1.extend(ll2)

        self.assertEqual(
            ll1,
            result
        )

        self.assertListEqual(
            values1 + values2,
            list(ll1)
        )

    def test_extend__when__second_list_is_empty__expect_extended_list(self):
        ll1 = ListInternal()
        ll2 = ListInternal()
        values1 = [1, 2, 3]
        values2 = []
        [ll1.append(v) for v in values1]
        [ll2.append(v) for v in values2]

        result = ll1.extend(ll2)

        self.assertEqual(
            ll1,
            result
        )

        self.assertListEqual(
            values1 + values2,
            list(ll1)
        )

    def test_extend__when__both_lists_are_empty__expect_empty_list(self):
        ll1 = ListInternal()
        ll2 = ListInternal()

        result = ll1.extend(ll2)

        self.assertEqual(
            ll1,
            result
        )

        self.assertListEqual(
            [],
            list(ll1)
        )

    def test_extend__when_second_param_is_not_iterable__expect_to_raise_type_error(self):
        ll1 = ListInternal()

        with self.assertRaises(TypeError) as context:
            ll1.extend(1)

        self.assertIsNotNone(context.exception)

    def test_insert__when_index_is_valid_in_the_middle__expect_to_insert_it(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4, 5])
        index = ll.size() // 2
        value = -100

        result = ll.insert(index, value)

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            [1, 2, value, 3, 4, 5],
            list(ll)
        )

    # same with negative indices
    def test_insert__when_index_is_0__expect_to_insert_it_at_the_start(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4, 5])
        index = 0
        value = -100

        result = ll.insert(index, value)

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            [value, 1, 2, 3, 4, 5],
            list(ll)
        )

    # same with negative indices
    def test_insert__when_index_is_size__expect_to_insert_it_at_the_end(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4, 5])
        index = ll.size()
        value = -100

        result = ll.insert(index, value)

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            [1, 2, 3, 4, 5, value],
            list(ll)
        )

    def test_insert__when_index_is_0_and_list_is_empty__expect_single_value(self):
        ll = ListInternal()
        index = 0
        value = -100

        result = ll.insert(index, value)

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            [value],
            list(ll)
        )

    def test_insert__when_index_is_greater_than_size__expect_to_raise_index_error(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4])
        index = ll.size() + 1
        value = -100

        with self.assertRaises(IndexError) as context:
            ll.insert(index, value)

        self.assertIsNotNone(context.exception)

    def test_insert__when_index_is_less_than_negative_size__expect_to_raise_index_error(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4])
        index = -ll.size() - 2
        value = -100

        with self.assertRaises(IndexError) as context:
            ll.insert(index, value)

        self.assertIsNotNone(context.exception)

    def test_insert_when_index_is_not_an_integer__expect_to_raise_type_error(self):
        ll = ListInternal()
        index = '1'
        value = -100

        with self.assertRaises(TypeError) as context:
            ll.insert(index, value)

        self.assertIsNotNone(context.exception)
        self.assertEqual(
            'Index should be an integer',
            str(context.exception)
        )

    def test_pop__when_list_is_empty__expect_to_raise_index_error(self):
        ll = ListInternal()
        with self.assertRaises(IndexError) as context:
            ll.pop()

        self.assertIsNotNone(context.exception)

    def test_pop__when_list_has_single_value__expect_to_return_last_value_and_empty_list(self):
        value = 1
        ll = self.__create_list_internal_with_values([value])

        result = ll.pop()

        self.assertEqual(
            value,
            result
        )

        self.assertListEqual(
            [],
            list(ll)
        )

    def test_pop__when_list_has_values__expect_to_return_last_value_and_correct_rest_values(self):
        value = 1
        values = list(range(4))
        ll = self.__create_list_internal_with_values(values + [value])

        result = ll.pop()

        self.assertEqual(
            value,
            result
        )

        self.assertListEqual(
            values,
            list(ll)
        )

    def test_clear__when_values_in_list__expect_empty_list(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4])

        ll.clear()

        self.assertListEqual(
            [],
            list(ll)
        )

    def test_clear__when_no_values_in_list__expect_empty_list(self):
        ll = ListInternal()

        ll.clear()

        self.assertListEqual(
            [],
            list(ll)
        )

    def test_index__when_value_in_list__expect_correct_index(self):
        value = -100
        ll = self.__create_list_internal_with_values([1, 2, value, 4, 5, 6])
        index = 2
        result = ll.index(value)

        self.assertEqual(
            index,
            result
        )

    def test_index__when_value_not_in_list__expect_to_raise_value_error(self):
        value = -100
        ll = self.__create_list_internal_with_values([1, 2, 4, 5, 6])
        with self.assertRaises(ValueError) as context:
            ll.index(value)

        self.assertIsNotNone(context.exception)

    def test_count__when_value_once_in_list__expect_1(self):
        value = -100
        ll = self.__create_list_internal_with_values([1, 2, 3, value, 4, 5])

        result = ll.count(value)

        self.assertEqual(
            1,
            result
        )

    def test_count__when_value_three_times_in_list__expect_3(self):
        value = -100
        ll = self.__create_list_internal_with_values([1, value, 2, value, 3, value, 4, 5])

        result = ll.count(value)

        self.assertEqual(
            3,
            result
        )

    def test_count__when_value_not_in_list__expect_0(self):
        value = -100
        ll = self.__create_list_internal_with_values([1, 2, 3, 4, 5])

        result = ll.count(value)

        self.assertEqual(
            0,
            result
        )

    def test_reverse__when_empty_list__expect_empty_list(self):
        ll = ListInternal()

        result = ll.reverse()

        self.assertListEqual(
            [],
            list(result)
        )

    def test_reverse__when_values_in_list__expect_list_with_reversed_values(self):
        values = list(range(1, 5))
        ll = self.__create_list_internal_with_values(values)

        result = ll.reverse()
        values.reverse()

        self.assertListEqual(
            values,
            list(result)
        )

    def test_copy__expect_list_with_same_values_diff_object(self):
        ll = self.__create_list_internal_with_values([1, 2, 3, 4, 5])

        result = ll.copy()

        self.assertListEqual(
            list(ll),
            list(result)
        )

        self.assertNotEqual(
            ll,
            result
        )

    def test_size__when_empty_list__expect_0(self):
        ll = ListInternal()

        self.assertEqual(
            0,
            ll.size()
        )

    def test_size__when_4_values_in_list__expect_4(self):
        values = [1, 2, 3, 4]
        ll = self.__create_list_internal_with_values(values)

        self.assertEqual(
            len(values),
            ll.size()
        )

    def test_len__when_empty_list__expect_0(self):
        ll = ListInternal()

        self.assertEqual(
            0,
            len(ll)
        )

    def test_len__when_4_values_in_list__expect_4(self):
        values = [1, 2, 3, 4]
        ll = self.__create_list_internal_with_values(values)

        self.assertEqual(
            len(values),
            len(ll)
        )

    def test_add_first__when_empty_list__expect_list_with_single_value(self):
        value = -100
        ll = ListInternal()

        ll.add_first(value)

        self.assertEqual(
            [value],
            list(ll)
        )

    def test_add_first__when_values_in_list__expect_list_with_value_at_start(self):
        value = -100
        values = list(range(5))
        ll = self.__create_list_internal_with_values(values)

        ll.add_first(value)

        self.assertEqual(
            [value] + values,
            list(ll)
        )

    def test_sum__when_empty_list__expect_0(self):
        ll = ListInternal()

        self.assertEqual(
            0,
            ll.sum()
        )

    def test_sum__when_list_with_values__expect_correct_sum(self):
        values = [1, 2, 3, 4, 5]
        ll = self.__create_list_internal_with_values(values)

        self.assertEqual(
            sum(values),
            ll.sum()
        )

    def test_sum__when_list_has_only_zeroes_expect_0(self):
        ll = self.__create_list_internal_with_values([0] * 5)

        self.assertEqual(
            0,
            ll.sum()
        )

    def test_underbound__when_empty_list__expect_to_raise_value_error(self):
        ll = ListInternal()

        with self.assertRaises(ValueError) as context:
            ll.underbound()

        self.assertIsNotNone(context.exception)

    def test_underbound__when_list_with_integers__expect_correct_result(self):
        value = -100
        values = [1, 2, 3, value, 4, 5]
        ll = self.__create_list_internal_with_values(values)

        index = values.index(value)

        result = ll.underbound()

        self.assertEqual(
            index,
            result
        )

    def test_underbound__when_list_with_len_objects__expect_correct_result(self):
        value = '1'
        values = ['12', value, [1, 2, 3], {'1': '2', '3': '4'}]
        ll = self.__create_list_internal_with_values(values)

        index = values.index(value)

        result = ll.underbound()

        self.assertEqual(
            index,
            result
        )

    def test_overbound__when_empty_list__expect_to_raise_value_error(self):
        ll = ListInternal()

        with self.assertRaises(ValueError) as context:
            ll.overbound()

        self.assertIsNotNone(context.exception)

    def test_overbound__when_list_with_integers__expect_correct_result(self):
        value = 100
        values = [1, 2, 3, value, 4, 5]
        ll = self.__create_list_internal_with_values(values)

        index = values.index(value)

        result = ll.overbound()

        self.assertEqual(
            index,
            result
        )

    def test_overbound__when_list_with_len_objects__expect_correct_result(self):
        value = '1234'
        values = ['12', value, [1, 2, 3], {'1': '2', '3': '4'}]
        ll = self.__create_list_internal_with_values(values)

        index = values.index(value)

        result = ll.overbound()

        self.assertEqual(
            index,
            result
        )

    def test_overbound__when_list_contains_non_integer_and_non_len_value__expect_to_raise_value_error(self):
        ll = self.__create_list_internal_with_values([1, 2, '123', ..., 3])

        with self.assertRaises(ValueError) as context:
            ll.overbound()

        self.assertIsNotNone(context.exception)

    def test_dictionize__when_empty_list__expect_empty_dict(self):
        ll = ListInternal()

        result = ll.dictionize()

        self.assertDictEqual(
            {},
            result
        )

    def test_dictionize__when_even_count_of_values__expect_correct_dict(self):
        size = 6
        values = list(range(1, size + 1))
        ll = self.__create_list_internal_with_values(values)

        result = ll.dictionize()
        expected_result = {
            1: 2,
            3: 4,
            5: 6,
        }

        self.assertDictEqual(
            expected_result,
            result
        )

    def test_dictionize__when_odd_count_of_values__expect_correct_dict(self):
        size = 5
        values = list(range(1, size + 1))
        ll = self.__create_list_internal_with_values(values)

        result = ll.dictionize()
        expected_result = {
            1: 2,
            3: 4,
            5: ' ',
        }

        self.assertDictEqual(
            expected_result,
            result
        )

    def test_move__when_count_is_less_than_len__expect_correct_result(self):
        values_1 = [1, 2, 3]
        values_2 = [4, 5, 6, 7, 8]
        ll = self.__create_list_internal_with_values(values_1 + values_2)

        result = ll.move(len(values_1))

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            values_2 + values_1,
            list(ll)
        )

    def test_move__when_count_is_0__expect_same_list(self):
        values = [1, 2, 3, 4, 5]
        ll = self.__create_list_internal_with_values(values)

        result = ll.move(0)

        self.assertEqual(
            ll,
            result
        )

        self.assertListEqual(
            values,
            list(ll)
        )

    def test_move__when_empty_list__expect_to_raise_index_error(self):
        ll = ListInternal()

        with self.assertRaises(IndexError) as context:
            ll.move(1)

        self.assertIsNotNone(context.exception)

    def test_move__when_count_is_negative__expect_to_raise_index_error(self):
        values = [1, 2, 3, 4, 5]
        ll = self.__create_list_internal_with_values(values)
        with self.assertRaises(IndexError) as context:
            ll.move(-1)

        self.assertIsNotNone(context.exception)

    def test_move__when_count_is_greater_than_list_len__expect_to_raise_index_error(self):
        values = [1, 2, 3, 4, 5]
        ll = self.__create_list_internal_with_values(values)
        with self.assertRaises(IndexError) as context:
            ll.move(ll.size() + 1)

        self.assertIsNotNone(context.exception)

    @staticmethod
    def __create_list_internal_with_values(values):
        ll = ListInternal()
        [ll.append(v) for v in values]
        return ll
