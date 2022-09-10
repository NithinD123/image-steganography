import cv2
import numpy as np

def DecimalToBinary(binary):
    b1 = bin(binary)
    b2 = b1[2:]
    if len(b2)<4:
        b = "0"*(4-len(b2))+b2 #zero padding on the left
    else:
        b = b2
        
    return b
    
def binaryToDecimal(binary):
     
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

def manupulation_bit(con,m,data):
    dec=DecimalToBinary(con)
    # taking another variable to delete the last two lsb bit and concatenate
    temp = int(dec[:len(dec)-2]+data[m]+data[m+1])
    binary = binaryToDecimal(temp)
    return binary
    
def manupulation_img_cd(arr,data):
    m = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            
            arr[i][j]= manupulation_bit(arr[i][j],m,data)
            m+=2
            if m>=len(data):
                return arr
    return arr

def manupulation_img_cd_color(arr,data):
    m = 0
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            
            arr[i][j]= manupulation_bit(arr[i][j],m,data)
            m+=2
            if m>=len(data):
                return arr
    return arr
    
def string_to_binary(string):
    
    res = ' '.join(format(ord(i), '08b') for i in string)
    return res

def binary_to_string(res):
    a_binary_string = res
    binary_values = a_binary_string.split()
    ascii_string = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character
    return ascii_string

def manupulation_cod_bit(con):
    dec=DecimalToBinary(con)
    # taking another variable to delete the last two lsb bit and concatenate
    temp_data = dec[len(dec)-2:]
    temp_img = int(dec[:len(dec)-2]+'01')
    binary_img = binaryToDecimal(temp_img)
    return binary_img, temp_data

def manupulation_cod_img(arr,si):
    m=0
    n = 0
    temp_data = ''
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] , temp = manupulation_cod_bit(arr[i][j])
            
            if n>si-1:
                return arr, temp_data
                   
            if m>=8:
                temp_data = temp_data+' '
                m=0
            if m<8:
                temp_data = temp_data+temp
                m=m+2
            n=n+1
        
    print(temp_data)
    return arr, temp_data


choice = int(input("Enter 1 to encode and 2 to decode : "))
n = input("Enter the path of the image : ")
m = input("Enter the name of the encripted/decripted image : ")
  
img = cv2.imread(n+'.png',0)
# cv2.imshow('original image',img)
# cv2.waitKey()

if choice == 1:
    p = input("Enter the secret image : ")
    s_img = cv2.imread(p+'.png',0)
    data1 = ''
    for i in range(len(s_img)):
        for j in range(len(s_img[i])):
            data1 = data1+chr(s_img[i][j])

    print(len(data1))
    print(data1)
    st_to_bi = string_to_binary(data1)
    print(st_to_bi)
    data = st_to_bi.translate({ord(' '): None})#used to remove the white space between bits 1110011 110011 as 1110011110011
    m_arr = manupulation_img_cd(img,data) 
    cv2.imwrite(m+'.png',m_arr)
elif choice ==2:
    size = int(input("Enter the size"))
    f_arr , f_data= manupulation_cod_img(img,(size)*4)
    data_str = binary_to_string(f_data)
    print('data',data_str)
    cv2.imwrite(m+'.png',f_arr)
else:
    print('wrong input')
