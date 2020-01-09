from utils import constants as const
from utils import generate_id as gen
from scripts import data_funcs as func
from scripts import Q_learning as qlearn
import random


class TestData() :

    # Constructor to initialize TestData object with given values
    def __init__(self,stock_data, prev_shares, prev_price, stocks,Q):
        self.prev_price = prev_price
        self.prev_shares = prev_shares
        self.num_shares = prev_shares
        self.curr_price = prev_price
        self.init_num_shares = prev_shares
        self.stock_data = stock_data
        self.stocks = stocks
        self.Q = Q
        self.curr_state =[]

    def test_daily_data(self):
        for day in range(const.TEST_STARTING_DAY,const.TEST_END_DAY +1):
                self.num_shares = self.prev_shares
                self.curr_price = self.prev_price
                curr_val = func.get_total(self.num_shares, self.curr_price)
                self.curr_state = func.get_curr_state(self.num_shares, self.curr_price)
                curr_state_id = gen.generate_state_Id(self.curr_state)
               # print("current_state:::::")
                #print (self.curr_state)
                #print("current_state_id:::::")
                #print (curr_state_id)
                actions = func.get_actions(self.curr_state)
                #print("actions:::::")
                #print(actions)

                state_action = {}
                # in this for loop, we generate action_id for each action in actions and construct a dictionary of
                # action_id:percentage_of_shares
                for action in actions:
                    action_id = gen.generate_state_Id(action)
                    state_action[action_id] = action


                opt_Q_val = const.NEG_INFINITY
                action = None
                if curr_state_id in self.Q:
                    opt_action = None
                    print("Q_STRUCTURES::::::::")
                    print(self.Q)
                    for action_id in self.Q[curr_state_id].keys():
                        q_val = self.Q[curr_state_id][action_id]
                      #  print("Q action_id keys::::::::")
                       # print(self.Q[curr_state_id].keys())
                        #print("q_val::::::::::")
                        #print((q_val))
                        #for each action in a state, we compare q_values
                        # and select the max Q_value
                        if q_val > opt_Q_val and action_id in state_action:
                         #   print("percentage of stocks for each action within a state")
                          #  print(state_action[action_id])

                            opt_Q_val = q_val
                            opt_action = state_action[action_id]

                    action = opt_action
                #chek if we dont get the optimal action value from the above logic
                #then we select the first action
                if opt_Q_val!=const.NEG_INFINITY and opt_Q_val < 0:
                    action = actions[0]
                #chek if we dont get the optimal action value from the above logic
                #then we randomly chose an action
                if action == None:
                    action = random.choice(actions)

                next_price = func.get_stock_prices(self.stock_data, self.stocks, day)
                self.next_num_shares = func.get_num_shares(action, self.curr_price, curr_val)
                self.next_val = func.get_total(self.next_num_shares, next_price)
                init_val = func.get_total(const.INITIAL_STOCK_SHARES,next_price)

                qlearn.q_learning(self.Q,self.curr_state, init_val, self.next_val, action, const.LEARNING_RATE)


               # print ("Action : ", action)
               # print (self.next_num_shares)
               # print (self.next_val)
                self.prev_price = next_price
                self.prev_shares = self.next_num_shares

        # List of required values
        return [self.curr_state, self.next_num_shares, self.next_val]
