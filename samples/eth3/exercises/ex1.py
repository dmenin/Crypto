import os
os.getcwd()
import sys
sys.path.append(os.path.join(os.getcwd(),'src'))
import trie, utils, rlp

#%load_ext autoreload
#%autoreload 2

#initialize trie
state = trie.Trie('triedb', trie.BLANK_ROOT)
state.update('\x01\x01\x02', rlp.encode(['hello']))
print 'root hash', state.root_hash.encode('hex')
k, v = state.root_node
print 'root node:', [k, v]
print 'hp encoded key, in hex:', k.encode('hex')
