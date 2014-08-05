import rarfile
import sys

base=15008457593
pos1=[1, 4, 5, 8, 9, 11]
pos2=[2, 3, 6, 7, 10]

#Check pwd with only one bit mistake,this is the most possible one
#V1.0
def pwd_gen_11_1(func):
    def _pwd_gen_11_1(rf):
        for i in range(1, 12):
            for j in range(0, 9):
                if str(base)[i-1]!=str(j):
                #if i!=(base%(10**i)-base%(10**(i-1)))
                   pwd=str(base-base%(10**i)+base%(10**(i-1))+j*(10**i))
                   if func(rf, pwd)==1:
                       sys.exit()
    return _pwd_gen_11_1
    
#This is write after using 3,4,4 rule, I'd rather use the upper one
def pwd_gen_11_1_2(func):
    def _pwd_gen_11_1(rf):
        for i in pos1:
            for j in range(0, 9):
                if str(base)[i-1]!=str(j):
                #if i!=(base%(10**i)-base%(10**(i-1)))
                   pwd=str(base-base%(10**i)+base%(10**(i-1))+j*(10**i))
                   if func(rf, pwd)==1:
                       sys.exit()
        for i in pos2:
            for j in range(0, 9):
                if str(base)[i-1]!=str(j):
                #if i!=(base%(10**i)-base%(10**(i-1)))
                   pwd=str(base-base%(10**i)+base%(10**(i-1))+j*(10**i))
                   if func(rf, pwd)==1:
                       sys.exit()
    return _pwd_gen_11_1
    
def pwd_gen_12(func):
    pass

#@pwd_gen_11_1_2
@pwd_gen_11_1
def fun(rf, pwd):
    #rf=rarfile.RarFile(file)
    try:
        rf.extractall(path=None, members=None, pwd=pwd)
    except Exception, e:
        print pwd+' is wrong\r\n'
        return 0
    else:
        print pwd+' is correcct\r\n'
        return 1
    #rf.extractall(path=None, members=None, pwd=pwd)
    #f=rf.open('r')
    #for ft in f:
    #    print ft

if __name__=='__main__':
    file=r'E:\personal\coding\lug\15008457593.rar'
    rf=rarfile.RarFile(file)
    fun(rf)
