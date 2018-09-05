#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """

    cleaned_data = []

    ### your code goes here
    errors = []
    for i in range(0, len(ages)):
        errors.append(predictions[i] - net_worths[i])

    errors = sorted(errors)

    ten_percentile = len(errors)//10

    errors = errors[:len(errors)-ten_percentile]

    for i in range(0, len(ages)):
        error = predictions[i] - net_worths[i]
        if error in errors:
            cleaned_data.append((ages[i], net_worths[i], error))

    return cleaned_data

