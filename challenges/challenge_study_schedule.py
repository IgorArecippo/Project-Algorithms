def study_schedule(permanence_period, target_time):
    # Verifica se o target_time é None e retorna None caso seja
    if target_time is None:
        return None

    # Verifica se a lista de permanence_periods está vazia ou se alguma tupla
    # possui comprimento diferente de 2 ou se algum valor não é do tipo int
    if not permanence_period or any(
        len(period) != 2 or not all(isinstance(time, int) for time in period)
        for period in permanence_period
    ):
        return None

    count = 0
    # Itera sobre as tuplas de permanence_periods
    for entry_time, departure_time in permanence_period:
        # Incrementa o contador se o entry_time ou departure_time for igual ao target_time
        if entry_time == target_time or departure_time == target_time:
            count += 1
        # Incrementa o contador se o target_time estiver dentro do intervalo (entry_time, departure_time)
        elif entry_time <= target_time and departure_time >= target_time:
            count += 1

    # Retorna a quantidade de estudantes presentes para o target_time
    return count

    raise NotImplementedError
