

# Extracting state_ids from list which represents percentage of stocks in the portfolio
def generate_state_Id(state_list):
    unique_id = ""
    for state in state_list:
        bits = int(state / 5)
        if state % 5 != 0:
            bits += 2
        unique_id += chr(65+bits)
    return unique_id

