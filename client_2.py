from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

import json

group = PairingGroup('BN254')
pin=1234

# get master secret:
cs = None
x = None
U = None
y = None
token = None
A = None
with open('client_1.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    cs=group.deserialize(bytes(r['cs_ser']['__value__']))
    x=group.deserialize(bytes(r['x_ser']['__value__']))
    U=group.deserialize(bytes(r['U_ser']['__value__']))
    token=group.deserialize(bytes(r['token_ser']['__value__']))
    A=group.deserialize(bytes(r['A_ser']['__value__']))


with open('server_1.json', 'r', encoding='utf-8') as f: 
    r = json.load(f) 
    y=group.deserialize(bytes(r['y_ser']['__value__']))

cs_calc = token + pin * A
V = -(x + y)*(cs)
def to_json(python_object):                           
        return {'__class__': 'bytes',
                '__value__': list(python_object)} 

with open('client_2.json', 'w', encoding='utf-8') as f: 
    json.dump(group.serialize(V), f, default=to_json) 

