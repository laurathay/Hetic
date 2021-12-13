# ----------------------< Game rules constants  >-----------------------------------------------------------------------
# Rules can be parametrized by this globals constants
#
# Standard Farkle rules :
#  5 dices with 6 faces
#  1 & 5 are scoring
#  1 is scoring 100 pts
#  5 is scoring 50 pts
#
#  Bonus for 3 dices with the same value
#   3 ace is scoring 1000 pts
#   3 time the same dice value is scoring 100 pts signal the dice value

# Target total score to win by default
DEFAULT_TARGET_SCORE = 2000

# Number of dices by default in the set
DEFAULT_DICES_NB = 5
# Number of side of the dices used in the game
NB_DICE_SIDE = 6

# List of dice value scoring
LIST_SCORING_DICE_VALUE = [1, 5]
# List of associated score for scoring dice values
LIST_SCORING_MULTIPLIER = [100, 50]

# Trigger for multiple bonus
TRIGGER_OCCURRENCE_FOR_BONUS = 3
# Special bonus multiplier for multiple ace bonus
BONUS_VALUE_FOR_ACE_BONUS = 1000
# Standard multiplier for multiple dices value bonus
BONUS_VALUE_FOR_NORMAL_BONUS = 100


# -----------------------------------------------------------------------
# def roll_dice_set(nb_dice_to_roll):
#     dice_value_occurence_list = [0] * NB_DICE_SIDE
#     for n in range(nb_dice_to_roll):
#         dice_value = random.randint(1, NB_DICE_SIDE)
#         dice_value_occurence_list[dice_value - 1] += 1
    
#     return dice_value_occurence_list
# print(roll_dice_set(1200000))


#mon esssaie 

# def analyse_bonus_score(dice_value_occurence_list):
#     nb_dice_to_roll = 6

#     dice_value_occurence_list =[0] * NB_DICE_SIDE
#     for n in range(nb_dice_to_roll):
#         dice_value = random.randint(1, NB_DICE_SIDE)

#         if dice_value == 1:
#             return "100"
#         if dice_value == 5:
#             return "50"
#         if ((dice_value) *n) % 2 == 0:
#             return n * "100" 

#         dice_value_occurence_list[dice_value - 1] += 1
         
#     return analyse_bonus_score
# print(analyse_bonus_score([6, 0, 0, 0, 4, 1]))

# def analyse_standard_scrore(dice_value_occurence_list):
#     nb_dice_to_roll = 6

#     dice_value_occurence_list = [0] * NB_DICE_SIDE
#     for n in range(nb_dice_to_roll):
#         dice_value = random.randint(1, NB_DICE_SIDE)

#         if dice_value != 1 : 5:
#             return "nothing"

#     return analyse_standard_scrore
# print(analyse_standard_score[6, 0, 0, 0, 4, 1]))


#correction
def analyse_bonus_score(dice_value_occurence_list):
    score = 0
    for side_value_index, dice_value_occurence_list in enumerate(dice_value_occurence_list):
        nb_of_bonus = dice_value_occurence //THRESHOLD_BONUS
        if nb_of_bonus > 0:
            if side_value_index == 0: 
                bonus_multiplier = ACE_BONUS_MULTIPILIER
            else:
                bonus_multiplier = STD_BONUS_MULTIPLIER
            score += nb_of_bonus * bonus_multiplier * (side_value_index + 1)
            dice_value_occurence_list[side_value_index] %= THRESHOLD_BONUS

        return score, dice_value_occurence_list


def analyse_standard_score(dice_value_occurrence_list):
    score = 0
    for scoring_value, scoring_multiplier in zip(SCORING_DICE_VALUE_LIST, SCORING_MULTIPLIER_LIST):
        score += dice_value_occurrence_list[scoring_value - 1] * scoring_multiplier
        dice_value_occurrence_list[scoring_value - 1] = 0

    return score, dice_value_occurrence_list


def analyse_score(dice_value_occurrence_list):
    bonus_score, dice_value_occurrence_list = analyse_bonus_score(dice_value_occurrence_list)
    standard_score, dice_value_occurrence_list = analyse_standard_score(dice_value_occurrence_list)

    return bonus_score + standard_score, dice_value_occurrence_list


print(analyse_score([7, 2, 3, 0, 4, 1]))