blockchain = [[1]]


def get_last_blockchain_value():
    """ Return the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = int(input("Yout tansaction amount: "))
    return user_input

def get_user_choice():
    user_input = int(input('Your choice: '))
    return user_input

def print_data(name, age, decade):
    print("Your data: ", name, ",", age, ", you live", decade, "decades.")

def main(args):
    # x = int(input("How many transaction?: "))
    # for i in range(x):
    #     tx_amount = get_user_input()
    #     add_value(tx_amount, get_last_blockchain_value())
    # print(blockchain)

    while True:
        print('Manu:')
        print('1: Add new transaction value: ')
        print('2. Print your blockchain: ')
        print('3. Finish loop:')
        user_choice = get_user_choice()
        if user_choice == 1:
            tx_amount = get_user_input()
            add_value(tx_amount, get_last_blockchain_value())
        elif user_choice == 2:
            print(blockchain)
        elif user_choice == 3:
            break
        else:
            print('Wrong choice!!')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
