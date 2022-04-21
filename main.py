from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

class Mpin(IBEnc):
    def __init__(self, groupObj):
        IBEnc.__init__(self)
        global group,h
        group = groupObj
        h = Hash(group)
        
    def setup(self):
        master_secret = group.random(ZR)
        client_key, server_key = group.random(G1),group.random(G2)
        return (master_secret, client_key, server_key)
    
    
    group = PairingGroup('BN254')
    s, P, = group.random(ZR), group.random(G2)

    ibe = IBE_BonehFranklin(group)
    print(ibe)