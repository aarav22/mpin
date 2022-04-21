from charm.toolbox.pairinggroup import PairingGroup,ZR,G1,G2,GT,pair
from charm.schemes.ibenc.ibenc_bf01 import IBE_BonehFranklin
from charm.toolbox.IBEnc import IBEnc
from charm.toolbox.hash_module import Hash,int2Bytes,integer

id="aarav.varshney@gmail.com"

group = PairingGroup('BN254')
master_secret = group.random(ZR)
client_key, server_key = group.random(G1),group.random(G2)
print(client_key, server_key)

# calculate A by hasing id to a point on G1:
A = group.hash(id, G1)
print(A)

# multiply master secret with A to get client secret:
client_secret = master_secret * A
server_secret = master_secret * server_key

# token calculation: (s - pin)A

# time permit:

# Authentication:
# client:
x = group.random(ZR)
U = x*A

# server:
y = group.random(ZR)

# client: 
V = -(x + y)*(client_secret)

# server:
g = pair(V, server_key) * pair(U + y*A, server_secret)
print(g)






