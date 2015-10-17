from btcturk_client.client import Btcturk

_btcturk = Btcturk("publicKey", "privateKey")

print 'balance', _btcturk.balance()
print 'transactions', _btcturk.transactions()
