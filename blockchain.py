blockchain = [[1]]


def get_last_blockchain_value():
    """ Return the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = int(input("Yout tansaction amount: "))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_data(name, age, decade):
    print("Your data: ", name, ",", age, ", you live", decade, "decades.")


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1

    return is_valid


def main(args):
    # x = int(input("How many transaction?: "))
    # for i in range(x):
    #     tx_amount = get_user_input()
    #     add_value(tx_amount, get_last_blockchain_value())
    # print(blockchain)

    while True:
        print('Manu:')
        print('1: Add new transaction value: ')
        print('2: Print your blockchain: ')
        print('h: Manipulate the chain')
        print('q: Finish loop:')
        user_choice = get_user_choice()
        if user_choice == '1':
            tx_amount = get_user_input()
            add_value(tx_amount, get_last_blockchain_value())
        elif user_choice == '2':
            print(blockchain)
        elif user_choice == 'h':
            if len(blockchain) >= 1:
                blockchain[0] = [2]
        elif user_choice == 'q':
            break
        else:
            print('Wrong choice!!')
        if not verify_chain():
            print("Invalid blockchain!")
            break

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
