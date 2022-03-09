from unittest import TestCase, main
from anagrams.anagrams import remove_non_letters
from anagrams.anagrams import word_processing
from anagrams.anagrams import reverse_text

# parametrization for class of TestRemoveNonLetter:
# set [(string, list_without_symbols)]
RemoveNonLetter_list_correct_IO_tuple = [("oKh=0dH]f!", ['o', 'K', 'h', 'd', 'H', 'f']),
                                         ("12345", []),
                                         ("DMPszKZ", ['D', 'M', 'P', 's', 'z', 'K', 'Z']),
                                         ("ПриВет_test", ['П', 'р', 'и', 'В', 'е', 'т', 't', 'e', 's', 't'])
                                         ]

# parametrization for class of TestWordProcessing:
# set [(string, reverse_string)] all non-letter symbols stay on the same places.
WordProcessing_list_correct_IO_tuple = [('a1bcd', 'd1cba'), ('Hi_Python_2021', 'no_htyPiH_2021'),
                                        ('Шалаш', 'шалаШ'), ('t;Z=%;D <X1"R*', 'R;X=%;D <Z1"t*'),
                                        ('https://coverage.readthedocs.io/en/coverage-5.1/',
                                         'egare://vocneois.codehtdaere.ga/re/vocsptth-5.1/')
                                        ]

# parametrization for class of TestReverseText:
# set [(text, reverse_text)] all non-letter symbols stay on the same places.
ReverseText_list_correct_IO_tuple = [('a1bcd efg!h', 'd1cba hgf!e'),
                                     ('welcome to the club 1423 buddy', 'emoclew ot eht bulc 1423 yddub'),
                                     ('Заказ Комок Радар Мадам', 'закаЗ комоК радаР мадаМ'),
                                     ('-)(i*$rrux}a[OM}HM~- xw)sA ', '-)(M*$HMOa}x[ur}ri~- As)wx '),
                                     ]

# parametrization for all classes:
# set [int, float, list, tuple, dict, set, bool]
list_wrong_type_words = [12345, 12.8845, ["ELopO Az14Tpn"], ('ab ct', 'cb 2a'),
                         {"a": '54', "b": '88'}, {'b', 'c', 'a'}, True
                         ]


class NonStringMixin:
    func_for_test_non_string = None

    def test_get_non_string(self):  # get [int, float, list, tuple, dict, set, bool]
        if self.func_for_test_non_string is None:
            raise ValueError("'func_for_test_non_string' should be set")
        for word_wrong_type in list_wrong_type_words:
            with self.subTest(msg="Checking raises 'TypeError' when word not string",
                              input_word=word_wrong_type, type_word=type(word_wrong_type)), \
                    self.assertRaises(TypeError):
                self.__class__.func_for_test_non_string(word_wrong_type)


class TestRemoveNonLetter(NonStringMixin, TestCase):
    func_for_test_non_string = remove_non_letters

    def test_return_correct_list(self):  # get [(string, list)]
        for word_type_string, result_list in RemoveNonLetter_list_correct_IO_tuple:
            with self.subTest(msg="Checking convert word_with_symbols to list_without_symbols",
                              word_with_symbols=word_type_string, list_without_symbols=result_list):
                self.assertEqual(remove_non_letters(word_type_string), result_list)


class TestWordProcessing(NonStringMixin, TestCase):
    func_for_test_non_string = word_processing

    def test_return_correct_reverse_string(self):
        for word, reverse_word in WordProcessing_list_correct_IO_tuple:
            with self.subTest(msg="Checking input: word, output: reverse word",
                              input_word=word, reverse_word=reverse_word):
                self.assertEqual(word_processing(word), reverse_word)


class TestReverseText(NonStringMixin, TestCase):
    func_for_test_non_string = reverse_text

    def test_return_correct_reverse_text(self):
        for text, inverted_text in ReverseText_list_correct_IO_tuple:
            with self.subTest(msg="Checking input: text, output: inverted text",
                              input_text=text, inverted_text=inverted_text):
                self.assertEqual(reverse_text(text), inverted_text)


if __name__ == "__main__":
    main()
