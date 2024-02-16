# import string_manipulations file
import string_manipulations


def test_integration_string_reverse_and_capitalization():
    # Apply capitalization_of_first_letters to "hello world" and then reverse the result
    result_1 = string_manipulations.reverse_string(string_manipulations.capitalization_of_first_letters("hello world"))
    expected_result_1 = "dlroW olleH"
    assert result_1 == expected_result_1


def test_integration_capitalization_and_string_reverse():
    # Apply reverse to "come here" and then capitalize the first letters of the result
    result_2 = string_manipulations.capitalization_of_first_letters(string_manipulations.reverse_string("come here"))
    expected_result_2 = "Erhe Emco"
    assert result_2 == expected_result_2


