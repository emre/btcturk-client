from btcturk_client.client import Btcturk

_btcturk = Btcturk("publickey", "privkey")

print _btcturk.balance()