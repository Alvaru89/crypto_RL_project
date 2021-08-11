import numpy as np
from my_env import Crypto_Env
import random


start_date="2014-01-01"
end_date="2021-07-06"
trial_dict = {'try': [],
              'prob_buy': [],
              'end_wallet':[],
              'max_reached':[]}
for i in range(0,100): #100 trials

    env = Crypto_Env()   # initialize our environment
    prob_buy = random.uniform(0.05,0.45)
    prob_sell=prob_buy
    prob_hold=1-prob_buy-prob_sell
    for days in range(2715): #days/steps between start and end date
        random_action = np.random.choice(np.arange(0, 3), p=[prob_buy, prob_sell, prob_hold])
        # random_coin = random.randint(0,3)
        amount = 2 #??????
        action_w = np.array([int(random_coin), int(random_action), amount])
        env.step(action_w)
        # env.render() no rendering required

    #recording results for later analysis and tuning
    trial_dict["try"].append(i)
    trial_dict['prob_buy'].append(prob_buy)
    trial_dict['end_wallet'].append([-1])
    trial_dict['max_reached'].append(max())

    trial_historic=

pd.DataFrame.from_dict(trial_dict).to_csv("output/trials_summary.csv")