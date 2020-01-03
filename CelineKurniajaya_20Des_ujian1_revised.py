#  Celine Kurniajaya JCDS07

# No 1

def Hashtag(string):
    jawaban=''
    listkata=string.split()
    # print(listkata)
    if len(listkata)==0:
        print('False')
    elif len(listkata)>=140:
        print('False')
    else:
        for item in listkata:
            if len(item)>=140:
                print('False')
            else:
        # print(item[0].capitalize()+item[1:])
                jawaban+=(item[0].capitalize()+item[1:])
        print('#'+jawaban)
    
(Hashtag('saya mau makan'))
(Hashtag('Hello    World'))
(Hashtag(''))
(Hashtag("   "))
(Hashtag('Hello there how are you doing'))
(Hashtag('Hello there how are you doing im fine but what about you i am sick no i am not okay but i miss you a b c d e f g h I j k l k h k n h n u I o g d b m k g e w f g n m o l o m o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o l o h t j k o l  g u j u g f b j o  h j j lk l j b h n j m j  fg v n m k j y bn m k n h g'))

# No 2

def create_phone_number(number):
    strng=[]
    tigaangkapertama=[]
    tigaangkakedua=[]
    lastangka=[]
    for i in number:
        strng.append(str(i))
    tigaangkapertama=(strng[0:3])
    tigaangkakedua=(strng[3:6])
    lastangka=(strng[6:])
    print('"'+'('+(''.join(tigaangkapertama))+')'+' '+(''.join(tigaangkakedua))+'-'+(''.join(lastangka))+'"')

create_phone_number([1,2,3,4,5,6,7,8,9,0])
create_phone_number([0,2,1,2,9,4,5,5,5,8])

#  no 3

def sort_odd_even(num):
    oddnumber=[]
    oddindex=[]
    evennumber=[]
    evenindex=[]
    all=[]
    indeksganjil={}
    indeksgenap={}
    for item in num:
        if item%2==0:
            evennumber.append(item)
            evenindex.append(num.index(item))
        else:
            oddnumber.append(item)
            oddnumber.sort()
            oddindex.append(num.index(item))
    evendescending=(sorted(evennumber, reverse=True))
    oddascending=(oddnumber)
    all=oddascending+evendescending
    for i,j in zip(oddascending,oddindex):
        indeksganjil[i]=j
    for item,nilai in zip(evendescending,evenindex):
        indeksgenap[item]=nilai
    for key,value in indeksgenap.items():
        all[value]=key
    for key,value in indeksganjil.items():
        all[value]=key
    print(all)

(sort_odd_even([5,3,0,2,8,1,4]))
(sort_odd_even([5,0,3,2,8,1,0,4]))
(sort_odd_even([5,3,2,8,1,4]))

#  no 4

def hollowtriangle(height) : 
    k = 0
    for i in range(1,height) :
      
        # Print spaces 
        for j in range(i,height) : 
            print('_', end='') 
          
        # Print # 
        while (k != (2 * i - 1)) : 
            if (k == 0 or k == 2 * i - 2) : 
                print('#', end='') 
            else : 
                print('_', end ='') 
            k = k + 1
        k = 0; 
        print ("_"*(height-1)) # print next row 
          
    # print last row 
    for i in range(0, 2 * height -1) : 
        print ('#', end = '') 



hollowtriangle(4)