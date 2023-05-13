whole_block = input("Input your block you want to encrypt:\n")


K1= int("dead",16)
K2= int("c0ff",16)
K3= int("ee5a",16)

block_l = int(whole_block[0:4],16)
block_r = int(whole_block[4:8],16)

block_r_4 = block_r & 0x000f
block_r_3 = (block_r & 0x00f0)>>4
block_r_2 = (block_r & 0x0f00)>>8
block_r_1 = (block_r & 0xf000)>>12


def reverse(bit):
    bit1 = (bit & 0b1000)>>3
    bit2 = (bit & 0b0100)>>1
    bit3 = (bit & 0b0010)<<1
    bit4 = (bit & 0b0001)<<3
    return(bit1|bit2|bit3|bit4)

def sbox(a):
    s_box = [0x4, 0x3, 0x9, 0xa, 0xb, 0x2, 0xe, 0x1, 0xd, 0xc, 0x8, 0x6, 0x7, 0x5, 0x0, 0xf]

    
    return s_box[a]


def feistelfunction(block_r_1,block_r_2,block_r_3,block_r_4):
    new_hex1 = (reverse(block_r_4))<<12
    new_hex2 = (sbox(block_r_2))<<8
    new_hex3 = (sbox(block_r_3))<<4
    new_hex4 = reverse(block_r_1)
    return(new_hex1|new_hex2|new_hex3|new_hex4)

test1 = feistelfunction(block_r_1,block_r_2,block_r_3,block_r_4)

def feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1):
    temp = feistelfunction(block_r_1,block_r_2,block_r_3,block_r_4)
    new = temp ^ K1
    res = new ^ block_l
    return(res)

test = feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1)

block_r_4_2 = feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1) & 0x000f
block_r_3_2 = (feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1) & 0x00f0)>>4
block_r_2_2 = (feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1) & 0x0f00)>>8
block_r_1_2 = (feistelround(block_r_1,block_r_2,block_r_3,block_r_4, K1) & 0xf000)>>12



def feistelround2(block_r_1_2,block_r_2_2,block_r_3_2,block_r_4_2, K2):
    temp = feistelfunction(block_r_1_2,block_r_2_2,block_r_3_2,block_r_4_2)
    new = temp ^ K2
    res = new ^ block_r
    return(res)

test1 = feistelround2(block_r_1_2,block_r_2_2, block_r_3_2,block_r_4_2, K2)


block_r_4_2_3 = (test1 & 0x000f)
block_r_3_2_3 = (test1 & 0x00f0)>>4
block_r_2_2_3 = (test1 & 0x0f00)>>8
block_r_1_2_3 = (test1 & 0xf000)>>12
# 

def feistelround3(block_r_1_2_3,block_r_2_2_3,block_r_3_2_3,block_r_4_2_3, K3):
    temp = feistelfunction(block_r_1_2_3,block_r_2_2_3,block_r_3_2_3,block_r_4_2_3)
    new = temp ^ K3
    res = new ^ test
    return(res)

test2= feistelround3(block_r_1_2_3,block_r_2_2_3,block_r_3_2_3,block_r_4_2_3, K3)

print(f"{hex(test1)[2:]}{hex(test2)[2:]}")