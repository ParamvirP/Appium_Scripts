import pytest


def fuzzy_math(num1, operator, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('We need to do fuzzy math on ints')

    if operator == '+':
        result = num1 + num2
    elif operator == '*':
        result = num1 * num2
    else:
        raise Exception(f"I don't know how to do math with that "
                        f"{operator} operator.")

    if result < 0:
        return 'A negative number, what does that even mean?'
    elif result < 10:
        return 'A small number, I can deal with that.'
    elif result < 20:
        return 'A medium sized number.'
    else:
        return 'A really big number, wayh too big for me!'


class TestFuzzyMath:

    def test_non_int_input_for_num1(self):
        with pytest.raises(Exception) as error:
            fuzzy_math('hi', "+", 2)
        assert 'We need to do fuzzy math on ints' in str(error)

    def test_non_int_input_for_num2(self):
        with pytest.raises(Exception) as error:
            fuzzy_math(2, "+", 'hi')
        assert 'We need to do fuzzy math on ints' in str(error)

    def test_addition_with_negative_result(self):
        assert fuzzy_math(-5, '+',
                          2) == 'A negative number, what does that even mean?'

    def test_addition_with_small_result(self):
        assert fuzzy_math(2, '+', 2) == 'A small number, I can deal with that.'

    def test_addition_with_medium_result(self):
        assert fuzzy_math(10, '+', 5) == 'A medium sized number.'

    def test_addition_with_large_result(self):
        assert fuzzy_math(
            10, '+', 10) == 'A really big number, wayh too big for me!'

    def test_multiply_with_negative_result(self):
        assert fuzzy_math(
            2, "*", -2) == 'A negative number, what does that even mean?'

    def test_multiply_with_small_result(self):
        assert fuzzy_math(2, "*", 2) == 'A small number, I can deal with that.'

    def test_multiply_with_medium_result(self):
        assert fuzzy_math(2, "*", 6) == 'A medium sized number.'

    def test_multiply_with_large_result(self):
        assert fuzzy_math(
            10, "*", 2) == 'A really big number, wayh too big for me!'

    def test_invalid_operator(self):
        with pytest.raises(Exception) as e:
            fuzzy_math(2, '/', 4)
        assert "don't know how to do math with that" in str(e)
