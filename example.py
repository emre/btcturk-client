from btcturk_client.client import Btcturk

_btcturk = Btcturk("publicKey", "privateKey")

print _btcturk.balance()