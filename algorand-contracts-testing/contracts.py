from algosdk import template


def _create_split_contract(owner, receiver_1, receiver_2, rat_1=1, rat_2=2, expiry_round=5000000,
                           min_pay=3000, max_free=2000):

    """Create and return split template instance from the provided arguments."""
    return template.Split(owner, receiver_1, receiver_2, rat_1, rat_2, expiry_round,
                          min_pay, max_free)


def _create_grouped_transactions(split_contract, amount):
    """Create grouped transactions for the provided 'split_contract' ana 'amount'."""
    params = suggested_params()
    return split_contract.get_split_funds_transaction(
        split_contract.get_program(), amount, 1,params.first, params.last, params.gh)


def create_split_transaction(split_contract, amount):
    """Create transaction with provided amount for provided split contract."""
    transactions = _create_grouped_transactions(split_contract, amount)
    transaction_id = process_transactions(transactions)
    return transaction_id


def _algod_client():
    '''Instantiate  and return algod client object.'''
    algod_address = "http://localhost:4001"
    algod_token = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    return algod.AlgodClient(algod_token, algod_address)

def process_trasactions(transactions):
    """Send provided grouped 'transactions' to network and wait  for  confirmation."""

