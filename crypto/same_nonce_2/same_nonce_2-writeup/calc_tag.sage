# SageMath version 10.1
#
# Installation Guide : https://github.com/sagemath/sage

def pad(x):
    return x + '00' * ((16-(len(x)//2)%16)%16)

def length(A, C):
    return ( int((len(A)//2)*8).to_bytes(8, byteorder='big') + int(len(C)//2 * 8).to_bytes(8, byteorder='big') ).hex().zfill(32)

def hex2poly(hexx, x):
    poly = 0
    binary = bin(int(hexx, 16))[2:].zfill(128)
    for i in range(len(binary)):
        poly += int(binary[i]) * x^i
    return poly

F, a = GF(2^128, name="a", modulus=x^128 + x^7 + x^2 + x + 1).objgen()
H = PolynomialRing(F, name="H").gen()

# exploit.py output
#
c1 = 'cd1c00af9dc5d174a6d81e80c210a8c7c59c78d3735af4e763'
t1 = 'dade2d1ea9c68edb3a064072c95717e0'
c2 = '76f7ce25f1a65c5c76f451891a089dfea5f64747782f46688a62224ec7d4bfca'
t2 = '031305b6357e50ec937bc75df54244a6'
c3 = '80f2c64aff2b086cb4e2918994c21de7ff4606e985a620c5db4ca3eaaccc8e41eb5696f2d5f1e9eecb9770f6939ca3'
#
# exploit.py output

A = ''# aad
l1= length(A, c1)
#l1 : [len(A)]_64 || [len(C1)]_64
l2= length(A, c2)
#l2 : [len(A)]_64 || [len(C2)]_64
l3= length(A, c3)
#l3 : [len(A)]_64 || [len(C3)]_64

l1 = hex2poly(l1, a)
l2 = hex2poly(l2, a)
l3 = hex2poly(l3, a)

c1 = pad(c1)
c2 = pad(c2)
c3 = pad(c3)

c1 = [c1[i:i+32] for i in range(0, len(c1), 32)]
c2 = [c2[i:i+32] for i in range(0, len(c2), 32)]
c3 = [c3[i:i+32] for i in range(0, len(c3), 32)] 

c1 = [hex2poly(c1[i], a) for i in range(0, len(c1))]
c2 = [hex2poly(c2[i], a) for i in range(0, len(c2))]
c3 = [hex2poly(c3[i], a) for i in range(0, len(c3))]

t1 = hex2poly(t1, a)
t2 = hex2poly(t2, a)

ciph_j = (c1[0]*H^3) + (c1[1]*H^2) + (l1*H) + t1    # CIPH(j0)
p = (c1[0] + c2[0])*H^3 + (c1[1] + c2[1])*H^2 + (l1 + l2)*H +(t1 + t2)
t3 = (c3[0]*H^4) + (c3[1]*H^3) + (c3[2]*H^2) + (l3*H) + ciph_j

tag_list = []
for H, m in p.roots():
    tag = t3(H)
    tag = str(int(bin(tag.to_integer())[2:].zfill(128)[::-1], 2).to_bytes(16, byteorder='big').hex())
    tag_list.append(tag)

for tag in tag_list:
    print(f'{tag}', end=' ') # exploit.py input
