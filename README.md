btcturk-client
================

python client for <a href="https://www.btcturk.com/yardim/api-home-page">btcturk api</a>.

### installation

```bash
$ (sudo) pip install btcturk_client
```

### usage
```python
from btcturk_client.client import Btcturk

_btcturk = Btcturk("publicKey", "privateKey")

# you can just init the Btcturk with zero arguments 
# if you don't plan to call authenticated api methods.
```

you can get your private/public key peer from your account at <a href="http://btcturk.com">BTCTurk</a>.

all methods including buy/sell are mapped to current API.

**example call: ticker()**

```python
from btcturk_client.client import Btcturk

print _btcturk.balance()
```

**response**

```javascript
{
    u 'Volume': 64.43,
    u 'Last': 889.85,
    u 'Timestamp': 1413890132.0,
    u 'Bid': 881.15,
    u 'High': 889.85,
    u 'Low': 872.15,
    u 'Ask': 885.0,
    u 'Open': 875.63
}
```

check out source for other methods.