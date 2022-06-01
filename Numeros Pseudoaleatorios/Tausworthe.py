from itertools import zip_longest

R = int(input("valor de r: "))
Q = int(input("valor de q: "))
Binario = int(input("valor de base binaria: "))

def operacionXOR(a,b):
  ab = 1
  if a  == b:
    ab = 0
  return ab

bits = []
b = (2 ** Q) - 1

for i in range(0,b):
  bits.append(0)

print(bits)

for i in range(0, Q):
  bits[i] = 1
  bits.append(1)

print(bits)

a = Q + 1
for i in range(a,len(bits)):
  i1 = i - R
  i2 = i - Q
  bits[i] = operacionXOR(bits[i1],bits[i2])

print(bits)

def binarioADecimal(binario):
  a = 0
  p = (Binario - 1)
  for i in range(0,len(binario)):
    if binario[i] == 1:
      a += 2**(p-i)
  return a
test_list = bits

def elementos(n, iterable, padvalue='1'):
    return zip_longest(*[iter(iterable)]*n, fillvalue=padvalue)

print("\n","It.", "\t", "Base 2", "\t","Base 10","\t","Ui","\n")
d = 0
for output in elementos(Binario, test_list):
    lst_new = [str(a) for a in output]
    print(d,"\t"," ".join(lst_new), "\t", binarioADecimal(output), "\t", "\t", binarioADecimal(output) / (2 ** Binario))
    d +=1