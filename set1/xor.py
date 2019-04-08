##cryptopals/set 1/challenge 2

a='1c0111001f010100061a024b53535009181c'
b='686974207468652062756c6c277320657965'
out='746865206b696420646f6e277420706c6179'
solution='746865206b696420646f6e277420706c6179'

if len(a) != len(b):
	exit(0)

aBinary=''
for i in a:
	aBinary+=bin(int(i,16))[2:].zfill(4)

bBinary=''
for i in b:
	bBinary+=bin(int(i,16))[2:].zfill(4)

#XOR
out=int(aBinary,2)^int(bBinary,2)

# Show outputs
print(aBinary)
print(bBinary)
print(bin(out)[2:].zfill(len(aBinary)))
print(hex(out)[2:])

if hex(out)[2:] == solution:
	print("OK!")
else:
    print("NOK")