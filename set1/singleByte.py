##cryptopals/set 1/challenge 3

import sys
import collections

##IC code from https://gist.github.com/enigmaticape/4254054
def ic_calculation(cipher_text):

   # remove all non alpha and whitespace and force uppercase
   # SOTHATCIPHERTEXTLOOKSLIKETHIS
   cipher_flat  = "".join( 
                           [x.upper() for x in cipher_text.split() \
                                      if  x.isalpha() ]
                        )

   # Tag em
   N            = len(cipher_flat)
   freqs        = collections.Counter( cipher_flat )
   alphabet     =  map(chr, range( ord('A'), ord('Z')+1))
   freqsum      = 0.0
   IC           = 0.0

   # Do the math
   for letter in alphabet:
       freqsum += freqs[ letter ] * ( freqs[ letter ] - 1 )

   if N > 1:
      IC = freqsum / ( N*(N-1) )
   
   return IC
   
#http://jdege.us/crypto-python/ar01s08.html#id2963591
english_ic = 0.0665
      
msg='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        
size=len(msg)
msgBinary=''
xored=''
for singleByte in range(0,255):
   for i in range(0,size,2):
      msgBinary=bin(int(msg[i:i+2],16))[2:].zfill(8)
      xored+=chr((int(msgBinary,2)^singleByte))
   index = ic_calculation(xored)
   if index > english_ic*0.90 and index < english_ic*1.10:
      print('Single Byte encoded by: '+chr(singleByte))
      print('Message: '+xored.strip()+'\n')
   xored=''