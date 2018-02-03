rpc_port=8545
host="http://localhost"
delay=0.0001
url = "{}:{}".format(host, rpc_port)
headers = {"content-type": "application/json"}

import requests
import json        
        
        
def _rpcRequest(method, params, key):
    """Make an RPC request to geth on port 8545."""
    payload = {
        "method": method,
        "params": params,
        "jsonrpc": "2.0",
        "id": 0
    }

    res = requests.post(
          url,
          data=json.dumps(payload),
          headers=headers).json()
    return res[key]



#1957e2 = 1660898
#4cAB3D = 5024573
data = _rpcRequest("eth_getBlockByNumber", ['0x4cAB3D', True], "result")
len(data['transactions'])

#SANDBOX



method = "eth_getBlockByNumber"
params = ['0x1b4', True]
key =  "result"


payload = {
    "method": method,
    "params": params,
    "jsonrpc": "2.0",
    "id": 0
}
res = requests.post(
      url,
      data=json.dumps(payload),
      headers=headers).json()
res
