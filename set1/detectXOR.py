##cryptopals/set 1/challenge 4

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
           

msgBinary=''
xored=''
with open('4.txt','r') as fileIn:
   for curline in fileIn:
      msg=curline.rstrip()
      size=len(msg)
      for singleByte in range(0,255): ##ASCII values for some printable letters
         for i in range(0,size,2):
            msgBinary=bin(int(msg[i:i+2],16))[2:].zfill(8)
            xored+=chr((int(msgBinary,2)^singleByte))
         index = ic_calculation(xored)
         if index > english_ic*0.50 and index < english_ic*1.50:
            print('Single Byte encoded by: '+chr(singleByte))
            print('Message: '+xored)
            print('Cypher: '+curline)
         xored=''