# Initializing {empty} blockchain list
MINING_REWARD = 10.0
genesis_block = {
        'previous_hash': '',
        'index': 0,
        'transactions': []
    }
blockchain = [genesis_block]
open_transactions = []
owner = 'LOL'
participants = {'LOL'}

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_recieved = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_recieved += tx[0]
    return amount_recieved - amount_sent

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
    participants.add(sender)
    participants.add(recipient)

def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    reward_transaction = {
        'sender': 'MINING',
        'recipient': owner,
        'amount': MINING_REWARD
    }
    open_transactions.append(reward_transaction)
    block = {
        'previous_hash': hashed_block,
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)
    return True

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
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index-1]):
            return False
    return True

def main(args):
    # x = int(input("How many transaction?: "))
    # for i in range(x):
    #     tx_amount = get_user_input()
    #     add_value(tx_amount, get_last_blockchain_value())
    # print(blockchain)

    while True:
        print('Manu:')
        print('1: Add new transaction value: ')
        print('2: Mine a new block')
        print('3: Print your blockchain: ')
        print('4: Output participants')
        print('h: Manipulate the chain')
        print('q: Finish loop:')
        user_choice = get_user_choice()
        if user_choice == '1':
            tx_data = get_transaction_value()
            recipient, amount = tx_data
            add_transaction(recipient, amount=amount)
        elif user_choice == '2':
            if mine_block():
                open_transactions = []
        elif user_choice == '3':
            print_blockchain_elements()
        elif user_choice == '4':
            print(participants)
        elif user_choice == 'h':
            if len(blockchain) >= 1:
                blockchain[0] = {
                    'previous_hash': '',
                    'index': 0,
                    'transactions': [{'sender': 'Chris', 'recipient': 'Max', 'amount': 100.0}]
                }
        elif user_choice == 'q':
            break
        else:
            print('Wrong choice!!')
        if not verify_chain():
            print_blockchain_elements()
            print("Invalid blockchain!")
            break
        print(get_balance('LOL'))
    else:
        print('User left!')

    print('DONE!')

    return 0


if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
