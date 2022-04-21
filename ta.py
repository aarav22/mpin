from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

import json
group = PairingGroup('BN254')

master_secret = group.random(ZR)
# save master_secret to a binary file:
# ta_file= open("ta.contxfig", "w") 
# ms_text = str(master_secret)
# print()
print(master_secret)
master_secret_ser = group.serialize(master_secret)
# encode master_secret to bytes:
def to_json(python_object):                           
        return {'__class__': 'bytes',
                '__value__': list(python_object)}                       

with open('entry.json', 'w', encoding='utf-8') as f: 
    json.dump(master_secret_ser, f, default=to_json) 
