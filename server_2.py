from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

import json
group = PairingGroup('BN254')

id="aarav.varshney@gmail.com"

# calculate A by hasing id to a point on G1:
A = group.hash(id, G1)

V = None
with open('client_2.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    V=group.deserialize(bytes(r['__value__']))

U = None
y = None
server_key = None
server_secret = None

with open('client_1.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    x=group.deserialize(bytes(r['x_ser']['__value__']))
    U=group.deserialize(bytes(r['U_ser']['__value__']))

with open('server_1.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    y=group.deserialize(bytes(r['y_ser']['__value__']))
    server_key=group.deserialize(bytes(r['sk_ser']['__value__']))
    server_secret=group.deserialize(bytes(r['ss_ser']['__value__']))


# compute g:
g=pair(V, server_key) * pair(U + y*A, server_secret)
# print(type(U), type(A), type(y), type(server_secret))
print(g)
