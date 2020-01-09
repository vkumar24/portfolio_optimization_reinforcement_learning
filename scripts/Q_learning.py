from utils import constants as const
from utils import generate_id as gen



# initializing q value from a state and all possible actions on the state
def initialize_Q(Q, state, actions):
    Q[str(state)] = {}
    for action in actions:
        Q[str(state)][str(action)] = 0

# returning q value from possible combinations of state action pair
def get_Q_val(Q, state, action):
    q_val = 0
    if str(state) in Q:
        if str(action) in Q[str(state)]:
            q_val = Q[str(state)][str(action)]
    return q_val

# adding new values to the q list
def add_Q_val(Q, state, action, val):
    if str(state) in Q:
        Q[str(state)][str(action)] = val
    else:
        Q[str(state)] = {str(action):val}

#updating q_value using
#list denoting current state
#initial value of portfolio
# next value of the portfolio
#list denoting action taken
# learning rate
def q_learning(Q, curr_state, init_val, next_val, actions, learning_rate):

    if next_val < init_val:
        reward = - init_val
    else:
        reward = next_val - init_val

    # calculating state_id from curr_state
    state_id = gen.generate_state_Id(curr_state)

    # calculating next_state_id from action taken
    list = []
    for i in str(actions).split("[")[1].split("]")[0].split(","):
        i = float(i)
        list.append(i)

    next_state_id = gen.generate_state_Id(list)
    #calculating old q value
    q_prev_state = get_Q_val(Q, state_id, next_state_id)

    #assuming optimum_q_value as -ve infinity
    opt_q_val = const.NEG_INFINITY



    if next_state_id in Q:
        for action in Q[next_state_id]:
            q_val = Q[next_state_id][action]
            if q_val > opt_q_val:
                opt_q_val = q_val
    if opt_q_val == const.NEG_INFINITY:
        opt_q_val = 0


    # Q-Learning equation
    final_q_val = q_prev_state + learning_rate * (reward + const.DISCOUNT_FACTOR * opt_q_val-q_prev_state)
    add_Q_val(Q, state_id, next_state_id, float(final_q_val))
