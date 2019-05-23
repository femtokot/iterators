def myrange(start, stop, step):

    current = start
    if step == 0:
        raise ValueError("Step should not be zero")

    if step > 0 and stop >= start:
        while current < stop:
            yield current
            current += step

    elif step < 0 and stop < start:
        while current > stop:
            yield current
            current += step

    return None