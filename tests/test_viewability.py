import pandas as pd
import pytest

from src.viewablity_eligibility import is_viewability_eligible


def read_csv_convert_to_dictionary(filepath):
    """
    Reads CSV file and convert into list of dictionaries.

    :param str filepath: The path to the CSV file.

    :return: list of dictionaries with each dictionary is a test case.

    :raises: FileNotFoundError: if file is not at given path.
    """
    try:
        test_cases_df = pd.read_csv(filepath)
        return test_cases_df.to_dict(orient="records")
    except FileNotFoundError as err:
        print(f"File at location {filepath} could not be found.")
        raise err


test_cases = read_csv_convert_to_dictionary("tests/test_data/scenarios.csv")


@pytest.mark.parametrize("test_case", test_cases)
def test_is_valid_impression(test_case):
    """
    Run test cases and compare actual output with expected output.
    :param dict test_case: dictionary representing individual test cases.
    :raises: AssertionError: if the result does not match expected value.
    """
    try:
        result = is_viewability_eligible(test_case['is_served'], test_case['time_spent'], test_case['GIVT'],
                                         test_case['vm'])
        assert result == test_case['expected'], f"failed for {test_case}"
    except AssertionError as err:
        print(f"test case {test_case} failed, expected : {test_case['expected']} actual {result}")
        raise err


if __name__ == "__main__":
    pytest.main()
