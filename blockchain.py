blockchain = [[1]]


def get_last_blockchain_value():
    """ Return the last value of current blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    blockchain.append([last_transaction, transaction_amount])


def get_user_input():
    user_input = int(input("Yout tansaction amount: "))
    return user_input


def print_data(name, age, decade):
    print("Your data: ", name, ",", age, ", you live", decade, "decades.")

def main(args):
    x = int(input("How many transaction?: "))

    for i in range(x):
        tx_amount = get_user_input()
        add_value(tx_amount, get_last_blockchain_value())

    print(blockchain)

    name = input("Your name: ")
    age = int(input("Yout age: "))
    decade = age//10;

    print_data(name, age, decade)
    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
