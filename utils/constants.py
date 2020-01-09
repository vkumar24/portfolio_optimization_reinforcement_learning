''' CONSTANT DECLARATION '''
#Training Data Range
TRAIN_STARTING_DAY = 0
TRAIN_END_DAY = 1005

#BackTest Data Range
TEST_STARTING_DAY = 1006
TEST_END_DAY = 1257

TRANSACTION_PERCENT = 5
EXPLORATION_ITERATIONS = 50


#Q_Learning Parameters
LEARNING_RATE = 0.9
DISCOUNT_FACTOR = 0.1
#Brokerage cost- 1%
BROKERAGE = 0.99

# Portfolio Stocks
STOCKS = ["AAPL","FB","GOOG","NFLX","TSLA"]
INITIAL_STOCK_SHARES = [20,2500,1200,145,2000]

#Optimum_Q initial value
NEG_INFINITY = float("-inf")
#Data Path
DATA_DIRECTORY = "../data/"

