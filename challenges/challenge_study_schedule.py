def study_schedule(permanence_period, target_time):
    if target_time is None:
        return None

    if not permanence_period or any(
        len(period) != 2 or not all(isinstance(time, int) for time in period)
        for period in permanence_period
    ):
        return None

    count = 0
    for entry_time, departure_time in permanence_period:
        if entry_time <= target_time <= departure_time:
            count += 1

    return count

    raise NotImplementedError
