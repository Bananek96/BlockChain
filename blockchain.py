# Initializing {empty} blockchain list
genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = []
open_transactions = []
owner = 'LOL'

def get_last_blockchain_value():
    """ Return the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with the transaction (default = 1.0).
    """

    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)

def mine_block():
    last_block = blockchain[-1]
    block = {
        'previous_hash': 'XYZ',
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)

def get_transaction_value():
    """Returns the input of the user (a new transaction amount) as float."""
    tx_recipient = input("Enter the recipient of the transaction: ")
    tx_amount = float(input("Yout tansaction amount: "))
    return (tx_recipient, tx_amount)


def get_user_choice():
    """Prompts the user fot its choice and return it."""
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """Output a;; blocks of the blockchain."""
    for block in blockchain:
        print('Outputting Block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """Verify the current blockchain and return True if it's valid"""
    # block_index = 0
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index-1]:
            is_valid = True
        else:
            is_valid = False
        #     break
        # block_index += 1

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
            tx_data = get_transaction_value()
            recipient, amount = tx_data
            add_transaction(recipient, amount=amount)
            print(open_transactions)
        elif user_choice == '2':
            print_blockchain_elements()
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
