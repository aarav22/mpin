from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

import json
group = PairingGroup('BN254')
server_key = group.random(G2)

# get master secret:
master_secret = None
with open('entry.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    print(r)
    print(bytes(r['__value__']))
    print(group.deserialize(bytes(r['__value__'])))
    master_secret=group.deserialize(bytes(r['__value__']))

# multiply master secret to get server_secret
server_secret = master_secret * server_key


y = group.random(ZR)
creds = {
    "y_ser": group.serialize(y),
    "sk_ser": group.serialize(server_key),
    "ss_ser": group.serialize(server_secret)
}

def to_json(python_object):                           
        return {'__class__': 'bytes',
                '__value__': list(python_object)}                       

with open('server_1.json', 'w', encoding='utf-8') as f: 
    json.dump(creds, f, default=to_json) 
