from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

import json

id="aarav.varshney@gmail.com"

group = PairingGroup('BN254')
client_key = group.random(G1)

# calculate A by hasing id to a point on G1:
A = group.hash(id, G1)
print(A)

# get master secret:
master_secret = None
with open('entry.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    print(r)
    print(bytes(r['__value__']))
    print(group.deserialize(bytes(r['__value__'])))
    master_secret=group.deserialize(bytes(r['__value__']))


# multiply master secret with A to get client secret:
client_secret = master_secret * A


# token calculation: (s - pin)A

# time permit:

# Authentication:
# client:
x = group.random(ZR)
U = x*A

# save cs, x and U to json:
cs_ser = group.serialize(client_secret)
x_ser = group.serialize(x)
U_ser = group.serialize(U)

creds = {
    "cs_ser": cs_ser,
    "x_ser": x_ser,
    "U_ser": U_ser,
}

# encode master_secret to bytes:
def to_json(python_object):                           
        return {'__class__': 'bytes',
                '__value__': list(python_object)}                       

with open('client_1.json', 'w', encoding='utf-8') as f: 
    json.dump(creds, f, default=to_json) 


