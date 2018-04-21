#ceasar cypher

global enc_out
global dec_out
enc_out = []
dec_out = []

def encode(text,num):
    split_txt = text.split()
    for a in split_txt:
        if len(a) > 1:
            list_a = list(a)
            for b in list_a:
                enc_chr = ord(b) + num
                enc_out.append(chr(enc_chr))
        else:
            enc_chr = ord(a) + num
            enc_out.append(chr(enc_chr))

def decode(text,num):
    split_txt = text.split()
    for a in split_txt:
        if len(a) > 1:
            list_a = list(a)
            for b in list_a:
                dec_chr = ord(b) + num*-1
                dec_out.append(chr(dec_chr))
        else:
            dec_chr = ord(a) + num*-1
            dec_out.append(chr(dec_chr))

inptext = input('Enter the text you wish to encode or decode ')
decision = input('press "E" for encode or "D" for decode ')
inpnum = int(input('enter the encode or decode number ex-12: '))

if decision.lower() == 'e':
    encode(inptext,inpnum)
    print('this is the encode result: ')
    print(''.join(enc_out))

elif decision.lower() == 'd':
    decode(inptext,inpnum)
    print('this is the decode result: ')
    print(''.join(dec_out))
