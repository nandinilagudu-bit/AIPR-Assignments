def calculate_average(scores):
    """Return the average of the scores."""
    total = 0
    for s in scores:
        total += s
    return total / len(scores)


def find_highest(scores):
    """Return the highest score."""
    highest = scores[0]
    for s in scores:
        if s > highest:
            highest = s
    return highest

def find_lowest(scores):
    """Return the lowest score."""
    lowest = scores[0]
    for s in scores:
        if s < lowest:
            lowest = s
    return lowest


def process_scores(scores):
    """Process scores and print average, highest and lowest."""
    avg = calculate_average(scores)
    highest = find_highest(scores)
    lowest = find_lowest(scores)

    print("Average:", avg)
    print("Highest:", highest)
    print("Lowest:", lowest)

scores = [80, 95, 70, 88, 92]
process_scores(scores)