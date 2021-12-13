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


# ----------------------------------------------------------------------------------------------------------------------
#mysterious_nb = random.randint(1, max_random)
#retourner l'occurence des dès avec une fonction 

#mon essaie
nb_dice_tr_roll = random.randit(1, 6)

        def roll():
            rolled = randrange(1, 6)
        if call_dice_set == 1 :
            return "1"
        if call_dice_set == 2 :
            return "2"
        if call_dice_set == 3 :
            return "3" 
        if call_dice_set == 4 :
            return "4"
        if call_dice_set == 5 :
            return "5"
        if call_dice_set == 6 :
            return "6"

def call_dice_set (nb_dice_tr_roll):
    nb_dice_tr_roll = 0

    index = 0
    while index < len(nb_dice_tr_roll[index])
        if roll() == N :
            List = [0] * N 
            print ("Il y a ", N, "fois ce dés")
        index += 1


    return call_dice_set(3, 1, 4, 5, 6, 2)

#correction 
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurence_list[dice_value - 1] += 1
    
    return dice_value_occurence_list
print(roll_dice_set(1200000))