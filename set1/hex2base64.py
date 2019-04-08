##cryptopals/set 1/challenge 1

str='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
solution='SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

base64={
0:"A",	16:"Q",	32:"g",	48:"w",
1:"B",	17:"R",	33:"h",	49:"x",
2:"C",	18:"S",	34:"i",	50:"y",
3:"D",	19:"T",	35:"j",	51:"z",
4:"E",	20:"U",	36:"k",	52:"0",
5:"F",	21:"V",	37:"l",	53:"1",
6:"G",	22:"W",	38:"m",	54:"2",
7:"H",	23:"X",	39:"n",	55:"3",
8:"I",	24:"Y",	40:"o",	56:"4",
9:"J",	25:"Z",	41:"p",	57:"5",
10:"K",	26:"a",	42:"q",	58:"6",
11:"L",	27:"b",	43:"r",	59:"7",
12:"M",	28:"c",	44:"s",	60:"8",
13:"N",	29:"d",	45:"t",	61:"9",
14:"O",	30:"e",	46:"u",	62:"+",
15:"P",	31:"f",	47:"v",	63:"/"
}

z=''
for i in str:
	z+=bin(int(i,16))[2:].zfill(4)
	
if len(z)%6 != 0:
	exit(0)

size=len(z)
base=''
for byte in range(0,size,6):
	base+=base64[int(z[byte:byte+6],2)]
	
print(base)

if base == solution:
	print("OK!")
else:
    print("NOK")