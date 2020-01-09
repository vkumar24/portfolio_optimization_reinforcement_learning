import random
from utils import constants as const
from utils import generate_id as gen
from scripts import data_funcs as func
from scripts.training_daily_data import TrainData
from scripts.testing_daily_data import TestData


def main():
    #Initializing varibales
    Q = {}
    stock_data = func.retrieve_stock_prices()
    print(stock_data)
    stocks = const.STOCKS
    num_shares = const.INITIAL_STOCK_SHARES
    curr_price = func.get_stock_prices(stock_data, stocks, const.TRAIN_STARTING_DAY)
    curr_state = func.get_curr_state(num_shares, curr_price)
    curr_state_id = gen.generate_state_Id(curr_state)

    print("INITIAL VALUES:::::::::::::::::::::::")
    print("Initial State::::", curr_state)
    print("Initial Id:::::", curr_state_id)

    ''' Iterate to Explore '''
    for itr in range(1, const.EXPLORATION_ITERATIONS):
        print("Explore Iteration : ", itr)

        #   assigning random share values to the 5 stocks
        share_a = random.randrange(0, 20, 4)
        share_b = random.randrange(0, 2500, 25)
        share_c = random.randrange(0, 1200, 12)
        share_d = random.randrange(0, 150, 15)
        share_e = random.randrange(0, 2000, 100)
        prev_shares = [share_a, share_b, share_c, share_d, share_e]
        prev_price = func.get_stock_prices(stock_data, stocks, 0)
        # Call TrainData object and provide the values for initialization
        train_data = TrainData(stock_data, prev_shares, prev_price, stocks, Q)
        # using train_data object call the training function which will run training on the data
        curr_price = train_data.train_daily_data()

    #print("Length of Q States ", len(Q.keys()))
    print("******************************")
    prev_shares = const.INITIAL_STOCK_SHARES
    prev_price = func.get_stock_prices(stock_data, stocks, const.TRAIN_END_DAY)
    curr_val = func.get_total(prev_shares, curr_price)
    curr_state = func.get_curr_state(prev_shares, curr_price)
   # print(curr_state, curr_val)
    print("******************************")

    # Call TestData object and provide the values for initialization
    test_data = TestData(stock_data, prev_shares, prev_price, stocks, Q)
    # using test_data object call the testing function which will run testing on the data
    result = test_data.test_daily_data()
    curr_state = result[0]
    next_num_shares = result[1]
    next_val = result[2]
    print("BACKTESTING::::::::::::::::::::::::::")
    print("State::::", curr_state)
    print("Number of Shares::::", next_num_shares)
    print("Value::::", next_val)

    print("BENCHMARK VALUES:::::::::::::::::::::")
    print("TRAIN_STARTING_DAY::::",
          func.get_total(const.INITIAL_STOCK_SHARES, func.get_stock_prices(stock_data, stocks, const.TRAIN_STARTING_DAY)))
    print("TRAIN_END_DAY::::",
          func.get_total(const.INITIAL_STOCK_SHARES, func.get_stock_prices(stock_data, stocks, const.TRAIN_END_DAY)))
    print("TEST_END_DAY:::::",
          func.get_total(const.INITIAL_STOCK_SHARES, func.get_stock_prices(stock_data, stocks, const.TEST_END_DAY)))

    #print(Q)
    return next_val


if __name__ == "__main__":
    main()

