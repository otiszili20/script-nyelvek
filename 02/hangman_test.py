import unittest
from parameterized import parameterized
from hangman import get_all_index


class HangmanTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_all_index_should_return_empty_if_there_is_no_match(self):
        # Given
        text = 'b'
        word = 'a'
        expected = []
        # When
        actual = get_all_index(text,word)
        # Then
        self.assertEqual(expected, actual)

    def test_get_all_index_should_return_zero_for_a_single_letter_matching_string(self):
        # Given
        text = 'a'
        word = 'a'
        expected = [0]
        # When
        actual = get_all_index(text,word)
        # Then
        self.assertEqual(expected,actual)

    def test_get_all_index_should_return_two_and_three_for_letter_l_in_word_hello(self):
        # Given
        text = 'l'
        word = 'hello'
        expected = [2,3]
        # When
        actual = get_all_index(text,word)
        # Then
        self.assertEqual(expected,actual)

    def test_get_all_index_should_raise_value_error_if_text_is_empty(self):
        # Given
        text = ''
        word = 'hello'
        # When Then
        with self.assertRaises(ValueError):
            get_all_index(text,word)

    def test_get_all_index_should_raise_value_error_if_text_is_longer_than_one_character(self):
        # Given
        text = 'ab'
        word = 'hello'
        # When Then
        with self.assertRaises(ValueError):
            get_all_index(text,word)

    # def test_get_all_index_should_raise_type_error_it_text_is_integer(self):
    #     # Given
    #     text = 1
    #     word = 'hello'
    #     # When Then
    #     with self.assertRaises(TypeError):
    #         get_all_index(text,word)
    #
    # def test_get_all_index_should_raise_type_error_it_text_is_list(self):
    #     # Given
    #     text = [1]
    #     word = 'hello'
    #     # When Then
    #     with self.assertRaises(TypeError):
    #         get_all_index(text,word)

    @parameterized.expand([
        (1,),
        ([1],),
        (1+3j,)
    ], skip_on_empty=True)
    def test_get_all_index_should_raise_type_error_if_text_is_not_str(self, text):
        word = 'hello'
        self.assertRaises(TypeError, get_all_index, text, word)

if __name__ == '__main__':
    unittest.main()