blockchain = []


def get_last_blockchain_value():
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction):
    if last_transaction is None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
    print(blockchain)


def get_transaction_value():
    return float(input('Your transaction amount, please: '))


def get_user_choice():
    return input('Your choice: ')


def output_blockchain_blocks():
    print('Outputting blocks...')

    for block in blockchain:
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    for block_idx in range(len(blockchain)):
        if block_idx == 0:
            continue
        if blockchain[block_idx][0] != blockchain[block_idx - 1]:
            return False
    return True


user_choice = None

while user_choice != 'q':
    print('Please choose:')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')

    user_choice = get_user_choice()

    if user_choice == '1':
        add_value(transaction_amount=get_transaction_value(), last_transaction=get_last_blockchain_value())
    elif user_choice == '2':
        output_blockchain_blocks()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice != 'q':
        print('Invalid option! Please choose an option from the list')

    if not verify_chain():
        print('Invalid blockchain!')
        break
else:
    print('Exiting program...')
