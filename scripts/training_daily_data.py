from utils import constants as const
from utils import generate_id as gen
from scripts import data_funcs as func
import random
from scripts import Q_learning as qlearn


class TrainData() :

    # Constructor function(init) to initialize properties of class TrainData
    # self is the object of the current instance, which gets initialized in init function
    def __init__(self,stock_data, prev_shares, prev_price, stocks,Q):
        self.prev_price = prev_price
        self.prev_shares = prev_shares
        self.num_shares = prev_shares
        self.curr_price = prev_price
        self.init_num_shares = prev_shares
        self.stock_data = stock_data
        self.stocks = stocks
        self.Q = Q

    def train_daily_data(self):
        ''' Trading over daily data '''
        for day in range(const.TRAIN_STARTING_DAY+ 1,const.TRAIN_END_DAY):
                self.num_shares = self.prev_shares
                self.curr_price = self.prev_price
                curr_val = func.get_total(self.num_shares, self.curr_price)
                curr_state = func.get_curr_state(self.num_shares, self.curr_price)
                actions = func.get_actions(curr_state)

                #Selecting random action from list of actions
                action = random.choice(actions)

                # Moving to the new state after selecting an action
                curr_state_id = gen.generate_state_Id(curr_state)
                next_price = func.get_stock_prices(self.stock_data, self.stocks, day)
                next_num_shares = func.get_num_shares(action, self.curr_price, curr_val)
                next_val = func.get_total(next_num_shares, next_price)
                init_val = func.get_total(self.init_num_shares, next_price)

                qlearn.q_learning(self.Q,curr_state, init_val, next_val, action, const.LEARNING_RATE)



                self.prev_price = next_price
                self.prev_shares = next_num_shares

        return self.curr_price
