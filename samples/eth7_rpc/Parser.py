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
    return res#[key]



#1957e2 = 1660898
#4cAB3D = 5024573
#data = 
data = _rpcRequest("eth_getBlockByNumber", ['0x1957e2', True], "result")['result']
#len(data['transactions'])

data2 = _rpcRequest("eth_getBlockByHash", [data['hash'], False], "result")['result']


_rpcRequest("eth_getTransactionByHash", [data2['transactions'][0]], "result")

_rpcRequest("eth_getTransactionByBlockHashAndIndex", [data2['transactions'][0], '0x0'], "result")#??
#eth_getTransactionByBlockNumberAndIndex??

transDataFromGetBlock = data['transactions'][0]
receipt = _rpcRequest("eth_getTransactionReceipt", [data2['transactions'][0]], "result")





_rpcRequest("net_listening", None, "result")




_rpcRequest("web3_clientVersion", ['0x1957e2', True], "result")


_rpcRequest("web3_sha3", ['0x68656c6c6f20776f726c64'], "result")


_rpcRequest("net_version", None, "result")
#{'id': 0, 'jsonrpc': '2.0', 'result': '4'} #"4": Rinkeby Testnet

_rpcRequest("net_listening", None, "result")
#True

_rpcRequest("net_peerCount", None, "result")
#0x1

_rpcRequest("eth_protocolVersion", None, "result")
#0x3f

_rpcRequest("net_listening", None, "result")
#True


_rpcRequest("eth_syncing", None, "result")
#False

_rpcRequest("eth_coinbase", None, "result")
#0xd6279d1693330b892537bb2ccd8649486e90396e

_rpcRequest("eth_mining", None, "result")
#False

_rpcRequest("eth_hashrate", None, "result")
#0

_rpcRequest("eth_gasPrice", None, "result") #0x77359400
_rpcRequest("eth_accounts", None, "result") #list of acc owned by the client
_rpcRequest("eth_blockNumber", None, "result") #most recent blocknumber


int(
_rpcRequest("eth_getBalance", ['0xd6279d1693330b892537bb2ccd8649486e90396e','latest'], "result")["result"]
, 0)/10e17
    
int(
_rpcRequest("eth_getBalance", ['0xd6279d1693330b892537bb2ccd8649486e90396e','0x1957e2'], "result")["result"]
, 0)/10e17

int(
_rpcRequest("eth_getBalance", ['0xd6279d1693330b892537bb2ccd8649486e90396e','0x0'], "result")["result"]
, 0)/10e17



int("0x13a550ad09b044000", 0)/10e17


_rpcRequest("eth_getStorageAt", None, "result") #????

#Returns the number of transactions sent from an address.
_rpcRequest("eth_getTransactionCount", ['0xd6279d1693330b892537bb2ccd8649486e90396e','0x1a4e71'], "result") 
#0x7

_rpcRequest("eth_getTransactionCount", ['0xd6279d1693330b892537bb2ccd8649486e90396e','latest'], "result") 
#0x8


#Transaction counts by block hash and number
data = _rpcRequest("eth_getBlockByNumber", ['0x1957e2', True], "result")['result']
len(data['transactions'])
#3
_rpcRequest("eth_getBlockTransactionCountByHash", [data['hash']], "result")
#0x3
_rpcRequest("eth_getBlockTransactionCountByNumber", ['0x1957e2'], "result")
#0x3

#Similar - Uncle count:
#eth_getUncleCountByBlockHash
#eth_getUncleCountByBlockNumber


#eth_getUncleByBlockHashAndIndex
#eth_getUncleByBlockNumberAndIndex


#contract code
_rpcRequest("eth_getCode", ['0x4D1CE458005ED9022E19B668a5F518ad3adAE757', 'latest'], "result")


#eth_sign
#eth_sendTransaction
#eth_sendRawTransaction
#eth_call
#eth_estimateGas

#eth_getCompilers
#eth_compileSolidity
#eth_compileLLL
#eth_compileSerpent

#eth_newFilter
#eth_newBlockFilter
#eth_newPendingTransactionFilter
#eth_uninstallFilter
#eth_getFilterChanges
#eth_getFilterLogs
#eth_getLogs







_rpcRequest("eth_getWork", None, "result")
#mining not ready: No work available yet, don't panic.

#eth_submitWork
#eth_submitHashrate



_rpcRequest("shh_version", None, "result")


_rpcRequest("net_listening", None, "result")

_rpcRequest("net_listening", None, "result")

_rpcRequest("net_listening", None, "result")





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
