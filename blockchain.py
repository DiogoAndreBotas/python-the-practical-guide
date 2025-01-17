MINING_REWARD = 10
GENESIS_BLOCK = {'previous_hash': '', 'index': 0, 'transactions': []}

blockchain = [GENESIS_BLOCK]
open_transactions = []
owner = 'Person 1'
participants = {'Person 1'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])


def get_balance(participant):
    transaction_sender = [
        [transaction['amount'] for transaction in block['transactions'] if transaction['sender'] == participant]
        for block in blockchain
    ]
    open_transaction_sender = [
        transaction['amount']
        for transaction in open_transactions
        if transaction['sender'] == participant
    ]
    transaction_sender.append(open_transaction_sender)
    amount_sent = 0

    for transaction in transaction_sender:
        if len(transaction) > 0:
            amount_sent += transaction[0]

    transaction_recipient = [
        [
            transaction['amount'] for transaction in block['transactions'] if transaction['recipient'] == participant
        ] for block in blockchain
    ]
    amount_received = 0
    for transaction in transaction_recipient:
        if len(transaction) > 0:
            amount_received += transaction[0]

    return amount_received - amount_sent


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    return get_balance(transaction['sender']) >= transaction['amount']


def verify_transactions():
    return all([verify_transaction(transaction) for transaction in open_transactions])


def add_transaction(recipient, sender=owner, amount=1.0):
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }

    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True

    return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    copied_transactions = open_transactions[:]

    copied_transactions.append(
        {
            'sender': 'MINING',
            'recipient': owner,
            'amount': MINING_REWARD
        }
    )

    blockchain.append(
        {
            'previous_hash': hashed_block,
            'index': len(blockchain),
            'transactions': copied_transactions
        }
    )
    return True


def get_transaction_data():
    return input('Recipient: '), float(input('Your transaction amount, please: '))


def get_user_choice():
    return input('Your choice: ')


def output_blockchain_blocks():
    print('Outputting blocks...')

    for block in blockchain:
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    for idx, block in enumerate(blockchain):
        if idx == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[idx - 1]):
            return False
    return True


user_choice = None

while user_choice != 'q':
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()
    if user_choice == '1':
        recipient, amount = get_transaction_data()
        if add_transaction(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        output_blockchain_blocks()
    elif user_choice == '4':
        print(participants)
    elif user_choice == '5':
        if verify_transactions():
            print('All transactions are valid!')
        else:
            print('There are invalid transactions!')
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '', 'index': 0,
                             'transactions': [{'sender': 'Person 1', 'recipient': 'Person 2', 'amount': '100'}]}
    elif user_choice != 'q':
        print('Invalid option! Please choose an option from the list')

    if not verify_chain():
        print('Invalid blockchain!')
        break

    print(get_balance('Person 1'))
else:
    print('Exiting program...')
