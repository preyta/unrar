import rarfile

base=[1, 5, 0, 0, 8, 4, 5, 7, 5, 9, 3]
def func(file, pwd):
    rf=rarfile.RarFile(file)
    try:
        rf.extractall(path=None, members=None, pwd=pwd)
    except Exception, e:
        print pwd+' is wrong\r\n'
    else:
        print pwd+' is correcct\r\n'
        return 0
    #rf.extractall(path=None, members=None, pwd=pwd)
    #f=rf.open('r')
    #for ft in f:
    #    print ft
        

def pwd_gen_11_1():
    pass
    
if __name__=='__main__':
    file='E:\url2.rar'
    psw='123456789'
    func(file, pwd)
