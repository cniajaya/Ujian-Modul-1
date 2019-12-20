#  Celine Kurniajaya JCDS07

# No 1

def Hashtag(string):
    jawaban=''
    listkata=string.split()
    # print(listkata)
    if len(listkata)==0:
        return False
    else:
        for item in listkata:
        # print(item[0].capitalize()+item[1:])
            jawaban+=(item[0].capitalize()+item[1:])
        print('#'+jawaban)
    
(Hashtag('saya mau makan'))
(Hashtag('Hello    World'))
(Hashtag(''))
(Hashtag('Hello there how are you doing'))

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
    allindex=[]
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
    # print(all)
    allindex=oddindex+evenindex
    # print(allindex)
    all[2]=8
    all[3]=4
    all[4]=5
    print(all)

sort_odd_even([5,3,2,8,1,4])

#  no 4

def hollowtriangle(height):
    triangle=[]
    if height==1:
        triangle.append('#')
        print(triangle)
    elif height==2:
        for item in range(height):
            triangle.append('-')
        triangle.insert(height-1,"#")
        print(''.join(triangle))
        print('#'*len(triangle))
    else:
        for item in range(1,height):
            triangle.append('-')
        for item in range(height-1):
            triangle.append('-')
        triangle.insert(height-1,"#")
        
        print(''.join(triangle))
        print('#'*(len(triangle)))

hollowtriangle(2)
hollowtriangle(3)
