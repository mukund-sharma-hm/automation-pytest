def is_viewability_eligible(is_served, time_spent, GIVT, vm):
    """
        Function to check if an impression in eligible according to viewability eligibility

        :param int is_served: 1 if the ad was served, 0 for ad not served.
        :param int time_spent: The time spent on the ad, should be greater than 0 for valid impression.
        :param int GIVT: 1 Indicates General invalid traffic, 0 indicates valid impression.
        :param int vm: Indicates viewability measurement, 1 for valid, 0 for invalid

        :return: 1 if the impression is valid else returns 0
    """

    if is_served == 1 and time_spent > 0 and GIVT == 0 and vm == 1:
        return 1
    return 0
