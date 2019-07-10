def determine_score(dice_values):

    # convert dice_values list into a dictionary
    
    dice_summary = {
        1: dice_values.count(1),
        2: dice_values.count(2),
        3: dice_values.count(3),
        4: dice_values.count(4),
        5: dice_values.count(5),
        6: dice_values.count(6),
    }

    pair_counter = 0

    is_a_straight = True

    for value,count in dice_summary.items():
        if count != 1:
            is_a_straight = False
        
        if count == 2:
            pair_counter += 1
        

    if is_a_straight:
        return 1500

    score = 0

    score += dice_summary[1] * 100
    score += dice_summary[5] * 50

    if pair_counter == 3:
        score = 1000
    
    return score