import pandas as pd
import pytest

from src.viewablity_eligibility import is_viewability_eligible


def read_csv_convert_to_dictionary(filepath):
    test_cases_df = pd.read_csv(filepath)
    return test_cases_df.to_dict(orient="records")


@pytest.fixture
def loaded_test_cases():
    test_cases = read_csv_convert_to_dictionary("tests/test_data/scenarios.py")
    return test_cases


@pytest.mark.parametrize("test_case",[None], indirect=True)
def test_is_valid_impression(test_case):
    result = is_viewability_eligible(test_case['is_served'], test_case['time_spent'], test_case['GIVT'],
                                     test_case['vm'])
    assert result == test_case['expected'], f"failed for {test_case}"

if __name__ == "__main__":
    pytest.main()