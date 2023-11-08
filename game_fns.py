import pygame as pg
import numpy as np

def set_completion_params(features = 3, bugs = 3): 
    params = dict()
    params['features'] = features
    params['bugs'] = bugs
    return params

def button_press(button_choice, event_name, event_key):
    # obtain the parameters
    bug_p = event_key.loc[event_name, 'bug_p']
    feature_p = event_key.loc[event_name, 'feature_p']
    debug_p = event_key.loc[event_name, 'debug_p']

    # roll the dice
    bug_outcome = dice_roll(bug_p)
    feature_outcome = dice_roll(feature_p)
    debug_outcome = dice_roll(debug_p)
        
    # record outcome
    outcomes = outcomes.append(
            [bug_outcome, feature_outcome, debug_outcome])

    # output outcome

    print("bug: " + str(bug_outcome))
    print(feature_outcome)
    print(debug_outcome)
    print(outcomes)


def dice_roll(param_prob):
    np.random.choice(
        [True, False],
        p = [param_prob, 1 - param_prob]    
    )   