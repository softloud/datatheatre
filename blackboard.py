import pandas as pd
import numpy as np

# get game event meta information
event_key = pd.read_csv("game-event-key.csv")

meeting = event_key.set_index('game_event')


bug_p = meeting.loc['meeting', 'bug_p']


bug_outcome = np.random.choice(
    [True, False],
    p = [bug_p, 1 - bug_p]    
)

bug_outcome = np.random.choice(
    [True, False],
    p = [bug_p, 1 - bug_p]    
)
