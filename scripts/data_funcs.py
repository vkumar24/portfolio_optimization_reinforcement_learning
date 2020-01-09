import itertools
import copy
from utils import constants as const
import os
import glob
import pandas as pd



def retrieve_stock_prices():
    data_set = {}
    dir_path = os.path.abspath(const.DATA_DIRECTORY)
    for file_path in glob.glob(os.path.join(dir_path,"*.csv")):
        file = pd.read_csv(file_path)
        file_name = os.path.basename(file_path).split(".csv")[0]
        data = []
        for i in file.index:
            data.append((file["Date"][i],file["Open"][i]))

        data_set[file_name] = data

    return data_set


# Extracting stock prices for each day
def get_stock_prices(data, stocks, day):
    price_list = []
    for stock in stocks:
        stock_val = data[stock][day][1]
        price_list.append(stock_val)
    return price_list

# Extracting state calculated based on the totalValue and input parameters.
def get_curr_state(num_shares, curr_price):
    total = get_total(num_shares, curr_price)
    curr_state = []
    length= len(num_shares)
    for i in range(length):
        weight = num_shares[i] * curr_price[i] / total
        share_percent = weight * 100
        curr_state.append(share_percent)
    return curr_state

# Extracting  list of Possible Actions on given state
def get_actions(states):
    actions = []
    actions.append(states)
    length= len(states)
    my_list = range(length)
    for i,j in itertools.combinations(my_list, 2):
            state_list1 = copy.deepcopy(states)
            state_list2 = copy.deepcopy(states)
            if state_list1[j] - const.TRANSACTION_PERCENT  >= 0 :
                state_list1[i] += const.TRANSACTION_PERCENT * const.BROKERAGE
                state_list1[j] -= const.TRANSACTION_PERCENT
                actions.append(state_list1)
            if state_list2[i] - const.TRANSACTION_PERCENT >= 0 :
                state_list2[j] += const.TRANSACTION_PERCENT* const.BROKERAGE
                state_list2[i] -= const.TRANSACTION_PERCENT
                actions.append(state_list2)
    return actions

# Extracting total value of the portfolio based on given input
def get_total(num_shares, curr_price):
    total = 0
    length= len(num_shares)
    for i in range(length):
        total += num_shares[i] * curr_price[i]
    return total

# Extracting list of 5 elements denoting the number
# of shares of each stock based on given input
def get_num_shares(lst,currentPrice,value):
    numShares = []
    for index in range(0,len(lst)):
        num = ((lst[index] / 100.0) * value) / currentPrice[index]
        numShares.append(num)
    return numShares





